--day 3 part 1 
--used clickhouse
with ld as (
	SELECT
		*
	FROM file ('2024_day3_input.txt', 'TSV', 'dl String')
),
extract_all as (
	select 
		arrayJoin(extractAll(dl, 'mul\(\\d+,\\d+\)')) as extracted
	from ld
),
nbrs as(
	select 
		splitByChar(',', arrayJoin(extractAll(extracted, '\\d+,\\d+'))) as nbrs_array 
	from extract_all
)
select sum(nbrs_array[1]::int * nbrs_array[2]::int) from nbrs


--day 3 part 2
with ld as (
	SELECT
		*
	FROM file ('2024_day3_input.txt', 'TSV', 'dl String')
),
extract_all as (
	select 
		row_number () over () as row_nbr,
		arrayJoin(extractAll(dl, 'mul\(\\d+,\\d+\)|don\'t\(\)|do\(\)')) as extracted
	from ld
),
do_do_not as (
	select
		*, case when extracted = 'don''t()' then 0
					when extracted = 'do()' then 1
						 end as do
	from extract_all
),
grouper as (
	select
		*, 
		count(do) over (order by row_nbr) as grouper
	from do_do_not as b
),
flt as (
select *, max(do) over (partition by grouper) as do_filter From grouper
),
nbrs as (
	select 
		splitByChar(',', arrayJoin(extractAll(extracted, '\\d+,\\d+'))) as nbrs_array 
	from flt
	where coalesce(do_filter, 1) = 1
and extracted <> 'do()'
)
select sum(nbrs_array[1]::int * nbrs_array[2]::int) from nbrs

