-- ---------------------------------------------------------------------------
-- System velocity versus observed velocity
-- ---------------------------------------------------------------------------
-- Inputs
--   velocity_observed                      the query in velocity_observed.sql,
--                                          materialised as a view
--   staging.mawm_item_facility_velocity    the WMS extract, one row per item
--                                          and facility, columns:
--                                            item_id, facility_id,
--                                            sku_velocity, extracted_at
--
-- Three statements below. Run them in order.
--   1. Row level variance, the working table
--   2. The confusion matrix, the one slide leadership will look at
--   3. Re-slot candidates ranked by what the mismatch is costing
--
-- READ THIS BEFORE INTERPRETING ANYTHING
-- A mismatch is only meaningful if the two sides were ever meant to mean the
-- same thing. Nobody currently knows what rule set the L, M and H values on
-- Item Facility, or when. Until that is known, disagreement here means "these
-- two numbers differ", not "the WMS is wrong". Getting the original thresholds
-- is a prerequisite, not a nice to have.
-- ---------------------------------------------------------------------------


-- 1. ------------------------------------------------------------------------
-- Row level variance
-- ---------------------------------------------------------------------------
create or replace view velocity_variance as

with system_side as (
    select
        item_id,
        facility_id,
        -- Normalise before comparing. Trailing spaces out of a UI grid export
        -- have sunk more than one reconciliation.
        nullif(upper(trim(sku_velocity)), '')     as system_velocity,
        extracted_at
    from staging.mawm_item_facility_velocity
),

joined as (
    select
        coalesce(o.facility_id, s.facility_id)    as facility_id,
        coalesce(o.item_id, s.item_id)            as item_id,
        o.description,
        o.product_class,
        s.system_velocity,
        o.observed_velocity,
        o.pick_lines,
        o.units_shipped,
        o.cumulative_share,
        o.no_movement_in_window,
        o.new_item,
        o.days_since_last_pick,
        o.spiky_single_order_item,
        s.extracted_at,
        case
            when s.item_id is null then 'moving, not in the WMS extract'
            when o.item_id is null then 'in the WMS extract, no movement data'
            else 'matched'
        end as coverage
    from velocity_observed o
    full outer join system_side s
        on  s.item_id     = o.item_id
        and s.facility_id = o.facility_id
)

select
    j.*,

    -- Rank the letters so direction of error can be described, not just
    -- presence of error. H is fast, L is slow.
    case j.system_velocity   when 'H' then 3 when 'M' then 2 when 'L' then 1 end
        as system_rank,
    case j.observed_velocity when 'H' then 3 when 'M' then 2 when 'L' then 1 end
        as observed_rank,

    case
        when j.system_velocity is null            then 'velocity not set in the WMS'
        when j.system_velocity not in ('H','M','L') then 'unexpected velocity value'
        when j.coverage <> 'matched'             then j.coverage
        when j.system_velocity = j.observed_velocity then 'agrees'
        when (case j.system_velocity when 'H' then 3 when 'M' then 2 else 1 end)
           < (case j.observed_velocity when 'H' then 3 when 'M' then 2 else 1 end)
            then 'understated: moves faster than the WMS thinks'
        else 'overstated: moves slower than the WMS thinks'
    end as verdict
from joined j;


-- 2. ------------------------------------------------------------------------
-- Confusion matrix. System velocity down the side, observed across the top.
-- The diagonal is agreement. Everything off it is the conversation.
-- ---------------------------------------------------------------------------
select
    facility_id,
    coalesce(system_velocity, '(not set)')                  as system_velocity,
    count_if(observed_velocity = 'H')                       as observed_H,
    count_if(observed_velocity = 'M')                       as observed_M,
    count_if(observed_velocity = 'L')                       as observed_L,
    count(*)                                                as items,
    sum(pick_lines)                                         as pick_lines,
    round(100.0 * sum(pick_lines)
          / nullif(sum(sum(pick_lines)) over (partition by facility_id), 0), 1)
        as pct_of_facility_pick_lines
from velocity_variance
where coverage = 'matched'
group by facility_id, coalesce(system_velocity, '(not set)')
order by facility_id, system_velocity;


-- 3. ------------------------------------------------------------------------
-- Re-slot candidates, most expensive first.
--
-- Ordered by pick lines, because an item the WMS calls slow while it is
-- actually the tenth busiest line in the building is costing travel on every
-- one of those picks. An item at the other end of the list is costing almost
-- nothing and is not worth touching.
--
-- The exclusions matter. A new item has not had time to establish a rate, and
-- an item whose whole window is one large order is not fast, it had one busy
-- day. Both would otherwise sit near the top of this list and both would be
-- wrong to re-slot.
-- ---------------------------------------------------------------------------
select
    facility_id,
    item_id,
    description,
    system_velocity,
    observed_velocity,
    verdict,
    pick_lines,
    units_shipped,
    round(100.0 * cumulative_share, 2) as cumulative_share_pct,
    days_since_last_pick
from velocity_variance
where verdict like 'understated%'
  and not coalesce(new_item, false)
  and not coalesce(spiky_single_order_item, false)
  and pick_lines > 0
order by pick_lines desc
limit 200;
