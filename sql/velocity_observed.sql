-- ---------------------------------------------------------------------------
-- Observed outbound velocity, per item and per facility
-- ---------------------------------------------------------------------------
-- Target: the WMS gold layer in Databricks. Dialect is Databricks SQL.
--
-- What this answers: how often is each item actually picked, and what velocity
-- class does that movement imply? This is the number the system velocity flag
-- on Item Facility is supposed to reflect, and the thing to compare it with.
--
-- WHY PICK LINES AND NOT UNITS OR DOLLARS
-- Velocity on Item Facility is a slotting attribute. Slotting cost is driven by
-- how many times a picker has to visit a location, not by how many units come
-- out of it when they get there. So the primary measure is pick lines. Units,
-- cases and value are carried alongside as secondary columns because they
-- answer different questions, and because the existing report named
-- "On Hand Velocity - Price" clearly weights by value, which is an inventory
-- question rather than a slotting one.
--
-- ASSUMED COLUMN NAMES
-- The gold table names are known. The column names below are assumed and must
-- be checked before this is run. Every one of them is listed here so it is a
-- five minute job against the catalogue rather than a debugging session:
--
--   outbound_lpn_detail : lpn_id, order_line_id, item_id, quantity
--   outbound_lpn        : lpn_id, facility_id, shipped_date, status
--   order_line          : order_line_id, order_id, item_id, line_type
--   item                : item_id, description, product_class, unit_price
--   facility            : facility_id, facility_name
--
-- GRAIN TO CONFIRM WITH THE WMS REPORTING CONTACTS
-- Is outbound_lpn_detail one row per pick, or one row per item per LPN with
-- picks already rolled up? If it is the latter, a single pick line spanning
-- two cartons counts twice and fast movers are overstated. This is the single
-- most important thing to confirm before anybody sees a number.
-- ---------------------------------------------------------------------------

with params as (
    select
        date_sub(current_date(), 90) as window_start,   -- rolling window
        current_date()               as window_end,
        0.80                         as h_share,        -- top 80% of pick lines
        0.95                         as m_share,        -- next 15%
        'ISP'                        as product_line    -- null for all lines
),

-- Shipped movement only. Cancelled and short shipped LPNs are not demand, and
-- counting them slots the warehouse for orders that never left.
shipped_lines as (
    select
        ol.facility_id,
        d.item_id,
        d.order_line_id,
        d.quantity,
        ol.shipped_date
    from outbound_lpn_detail d
    join outbound_lpn ol
        on ol.lpn_id = d.lpn_id
    cross join params p
    where ol.status in ('SHIPPED', 'CLOSED')
      and ol.shipped_date >= p.window_start
      and ol.shipped_date <  p.window_end
),

-- EXCLUSIONS TO CONFIRM. Replenishment, cycle count adjustments, returns to
-- stock and inter facility transfers all create movement that is not customer
-- demand. If order_line.line_type does not separate them, find the flag that
-- does before trusting any of this.
demand_lines as (
    select
        s.facility_id,
        s.item_id,
        s.order_line_id,
        s.quantity,
        s.shipped_date
    from shipped_lines s
    left join order_line l
        on l.order_line_id = s.order_line_id
    where coalesce(l.line_type, 'CUSTOMER') not in ('TRANSFER', 'REPLEN', 'ADJUST')
),

movement as (
    select
        d.facility_id,
        d.item_id,
        count(distinct d.order_line_id)         as pick_lines,
        sum(d.quantity)                         as units_shipped,
        count(distinct d.shipped_date)          as active_days,
        min(d.shipped_date)                     as first_shipped,
        max(d.shipped_date)                     as last_shipped
    from demand_lines d
    group by d.facility_id, d.item_id
),

-- Every item stocked at the facility, so items with no movement in the window
-- appear rather than silently disappearing. A missing row and a zero are very
-- different findings and this is where most velocity comparisons go wrong.
stocked as (
    select distinct
        ol.facility_id,
        d.item_id
    from outbound_lpn_detail d
    join outbound_lpn ol on ol.lpn_id = d.lpn_id
    -- REPLACE with the item facility table once it lands in gold. Until then
    -- this only sees items that have shipped at some point, which understates
    -- the slow end of the range.
),

base as (
    select
        s.facility_id,
        s.item_id,
        coalesce(m.pick_lines, 0)    as pick_lines,
        coalesce(m.units_shipped, 0) as units_shipped,
        coalesce(m.active_days, 0)   as active_days,
        m.first_shipped,
        m.last_shipped
    from stocked s
    left join movement m
        on m.facility_id = s.facility_id
       and m.item_id     = s.item_id
),

ranked as (
    select
        b.*,
        sum(b.pick_lines) over (partition by b.facility_id) as facility_pick_lines,
        sum(b.pick_lines) over (
            partition by b.facility_id
            order by b.pick_lines desc, b.item_id      -- item_id breaks ties
            rows between unbounded preceding and current row
        ) as running_pick_lines
    from base b
)

select
    r.facility_id,
    f.facility_name,
    r.item_id,
    i.description,
    i.product_class,
    r.pick_lines,
    r.units_shipped,
    r.active_days,
    round(r.pick_lines / nullif(datediff(p.window_end, p.window_start), 0), 3)
        as pick_lines_per_day,
    round(r.running_pick_lines / nullif(r.facility_pick_lines, 0), 6)
        as cumulative_share,

    -- Classified to match the letters used on Item Facility, not to ABC.
    -- H is the fast end. Note the direction trap: in ABC, A is fast; here H is
    -- fast. Anybody translating between the two will get it backwards once.
    case
        when r.pick_lines = 0                                                     then 'L'
        when r.running_pick_lines / nullif(r.facility_pick_lines, 0) <= p.h_share then 'H'
        when r.running_pick_lines / nullif(r.facility_pick_lines, 0) <= p.m_share then 'M'
        else 'L'
    end as observed_velocity,

    -- Flags that stop a mechanical re-slot doing something stupid.
    r.pick_lines = 0                                   as no_movement_in_window,
    r.first_shipped >= date_sub(p.window_end, 30)      as new_item,
    datediff(p.window_end, r.last_shipped)             as days_since_last_pick,
    r.active_days <= 2 and r.pick_lines > 0            as spiky_single_order_item,

    p.window_start,
    p.window_end
from ranked r
cross join params p
left join item     i on i.item_id     = r.item_id
left join facility f on f.facility_id = r.facility_id
where p.product_line is null
   or i.product_class = p.product_line
order by r.facility_id, r.pick_lines desc
