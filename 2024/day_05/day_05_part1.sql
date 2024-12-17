--day 5 part 1
--used clickhouse
with nbr_list as (
	select * from numbers(1, 200)
),
ld as (
	SELECT
	row_number() over () as row_nbr,
		*
	FROM file ('adoc/2024_day5_input.txt', 'TSV', 'dl String')
),
page_order as (
	select * from ld
	where dl like '%|%'
),
page_updates as (
	select * from ld
	where dl like '%,%'
),
split_pages as(
	select
	dl,
	number,
	splitByChar(',', dl)[number] as pages
	From page_updates
	join nbr_list on 0=0
	where number<= length(splitByChar(',', assumeNotNull(dl)))
),
page_update_order as (
	select dl, a.number, concat(a.pages,'|',b.pages) as pg_order from split_pages a
	join split_pages b on b.dl = a.dl and b.number = a.number + 1
),
update_counts as ( 
	select dl, count(pg_order) as cnt, sum(case when b.dl = '' then 0 else 1 end) as match_cnt from page_update_order a
	left join page_order b on b.dl = a.pg_order
	group by dl
),
correct_update as (
	select
		*, 
		case when cnt = match_cnt then 1 else 0 end as correct
	from update_counts
),
correct_update_with_middle as (
	select
		*,
		splitByChar(',', dl)[((length(splitByChar(',', dl))+1)/2)::Int] as mid_val
	from correct_update
)
select
	sum(mid_val::Int64)
from correct_update_with_middle
where correct = 1