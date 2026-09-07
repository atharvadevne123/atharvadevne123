// =====================================================================
//  Dim_Date
//  Paste into: Power BI Desktop > Home > Transform data >
//              New Source > Blank Query > Advanced Editor
//  Then rename the query to  Dim_Date
//
//  Adjust FiscalStartMonth if the fiscal year does not start in January.
//  CONFIRM the fiscal calendar with the business (Step 6).
// =====================================================================
let
    StartDate        = #date(2024, 1, 1),
    EndDate          = #date(2027, 12, 31),
    FiscalStartMonth = 1,

    DayCount = Duration.Days(EndDate - StartDate) + 1,
    Source   = List.Dates(StartDate, DayCount, #duration(1,0,0,0)),
    ToTable  = Table.FromList(Source, Splitter.SplitByNothing(), {"Date"}),
    TypeDate = Table.TransformColumnTypes(ToTable, {{"Date", type date}}),

    Today = Date.From(DateTime.LocalNow()),

    Added = Table.AddColumn(TypeDate, "Cols", each
        let
            d          = [Date],
            y          = Date.Year(d),
            m          = Date.Month(d),
            fiscalM    = Number.Mod(m - FiscalStartMonth, 12) + 1,
            fiscalY    = if m >= FiscalStartMonth then y else y - 1,
            monthStart = Date.StartOfMonth(d)
        in [
            Year            = y,
            Quarter         = "Q" & Text.From(Date.QuarterOfYear(d)),
            QuarterNumber   = Date.QuarterOfYear(d),
            MonthNumber     = m,
            MonthName       = Date.ToText(d, "MMMM"),
            MonthShort      = Date.ToText(d, "MMM"),
            MonthYear       = Date.ToText(d, "MMM yyyy"),
            MonthYearSort   = y * 100 + m,
            MonthStartDate  = monthStart,
            WeekOfYear      = Date.WeekOfYear(d, Day.Monday),
            WeekStartDate   = Date.StartOfWeek(d, Day.Monday),
            DayOfWeekNumber = Date.DayOfWeek(d, Day.Monday) + 1,
            DayName         = Date.ToText(d, "dddd"),
            DayShort        = Date.ToText(d, "ddd"),
            IsWeekend       = Date.DayOfWeek(d, Day.Monday) >= 5,
            IsWorkingDay    = Date.DayOfWeek(d, Day.Monday) < 5,
            FiscalYear      = fiscalY,
            FiscalMonth     = fiscalM,
            FiscalQuarter   = "FQ" & Text.From(Number.RoundUp(fiscalM / 3)),
            // Relative flags. Useful for default filters so the report opens
            // on something sensible instead of the whole history.
            IsPast          = d <= Today,
            IsLast30Days    = d <= Today and d > Date.AddDays(Today, -30),
            IsLast90Days    = d <= Today and d > Date.AddDays(Today, -90),
            IsLast12Months  = d <= Today and d > Date.AddMonths(Today, -12),
            IsCurrentMonth  = monthStart = Date.StartOfMonth(Today),
            IsCurrentYear   = y = Date.Year(Today)
        ]),

    Expanded = Table.ExpandRecordColumn(Added, "Cols",
        {"Year","Quarter","QuarterNumber","MonthNumber","MonthName","MonthShort",
         "MonthYear","MonthYearSort","MonthStartDate","WeekOfYear","WeekStartDate",
         "DayOfWeekNumber","DayName","DayShort","IsWeekend","IsWorkingDay",
         "FiscalYear","FiscalMonth","FiscalQuarter","IsPast","IsLast30Days",
         "IsLast90Days","IsLast12Months","IsCurrentMonth","IsCurrentYear"}),

    Typed = Table.TransformColumnTypes(Expanded, {
        {"Year", Int64.Type}, {"Quarter", type text}, {"QuarterNumber", Int64.Type},
        {"MonthNumber", Int64.Type}, {"MonthName", type text}, {"MonthShort", type text},
        {"MonthYear", type text}, {"MonthYearSort", Int64.Type},
        {"MonthStartDate", type date}, {"WeekOfYear", Int64.Type},
        {"WeekStartDate", type date}, {"DayOfWeekNumber", Int64.Type},
        {"DayName", type text}, {"DayShort", type text},
        {"IsWeekend", type logical}, {"IsWorkingDay", type logical},
        {"FiscalYear", Int64.Type}, {"FiscalMonth", Int64.Type},
        {"FiscalQuarter", type text}, {"IsPast", type logical},
        {"IsLast30Days", type logical}, {"IsLast90Days", type logical},
        {"IsLast12Months", type logical}, {"IsCurrentMonth", type logical},
        {"IsCurrentYear", type logical}
    })
in
    Typed
