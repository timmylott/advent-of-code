--day 1 part 1
--used clickhouse
with lt as (
	SELECT
		splitByChar(' ', assumeNotNull(c1))[1]::bigint as nbr,
		ROW_NUMBER() over (order by splitByChar(' ', assumeNotNull(c1))[1]::bigint) as row_nbr
	FROM file ('2024_day1_input.csv')
),
rt as (
	SELECT
		splitByChar(' ', assumeNotNull(c1))[4]::bigint as nbr,
		ROW_NUMBER() over (order by splitByChar(' ', assumeNotNull(c1))[4]::bigint) as row_nbr
	FROM file ('2024_day1_input.csv')
),
diff as (
	SELECT
		*,
		abs(lt.nbr - rt.nbr) as diff_nbr
	from lt
	join rt on rt.row_nbr = lt.row_nbr
) 
SELECT
	sum(diff_nbr)
from diff;


--day 1 part 2
with lt as (
	SELECT
		splitByChar(' ', assumeNotNull(c1))[1]::bigint as nbr,
		ROW_NUMBER() over (order by splitByChar(' ', assumeNotNull(c1))[1]::bigint) as row_nbr
	FROM file ('2024_input_day1.csv')
),
rt as (
	SELECT
		splitByChar(' ', assumeNotNull(c1))[4]::bigint as nbr,
		ROW_NUMBER() over (order by splitByChar(' ', assumeNotNull(c1))[4]::bigint) as row_nbr
	FROM file ('2024_input_day1.csv')
),
mlt as (
	SELECT
		nbr,
		count(*) mlt_nbr from rt
	group by nbr
)
select
	sum(
	lt.nbr * coalesce(mlt.mlt_nbr, 0)
	)
from lt
left join mlt on mlt.nbr = lt.nbr