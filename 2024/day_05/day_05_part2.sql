--day 5 part 1
--used clickhouse

with RECURSIVE  nbr_list as (
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
	select *, length(splitByChar(',', dl)) as len_dl from ld
	where dl like '%,%'
),
split_pages as(
	select
	dl,
	len_dl,
	number,
	splitByChar(',', dl)[number] as pages
	From page_updates
	join nbr_list on 0=0
	where number<= length(splitByChar(',', assumeNotNull(dl)))
),
page_update_order as (
	select dl, len_dl, a.number, concat(a.pages,'|',b.pages) as pg_order from split_pages a
	join split_pages b on b.dl = a.dl and b.number = a.number + 1
),
update_counts as ( 
	select dl, len_dl, count(pg_order) as cnt, sum(case when b.dl = '' then 0 else 1 end) as match_cnt from page_update_order a
	left join page_order b on b.dl = a.pg_order
	group by dl, len_dl
),
correct_update as (
	select
		*, 
		case when cnt = match_cnt then 1 else 0 end as correct
	from update_counts
),
not_correct AS (
	SELECT * FROM correct_update
	WHERE correct=0
),
not_correct_split AS (
	select
	dl,
	len_dl,
	number,
	splitByChar(',', dl)[number] as pages
	From not_correct
	join nbr_list on 0=0
	where number<= len_dl
),
not_correct_order as (
	select *, pages as p_from, splitByChar('|', b.dl)[2] as p_to  From not_correct_split a
	join page_order b on splitByChar('|', b.dl)[1] = a.pages
	where hasAny([splitByChar('|', b.dl)[2]], splitByChar(',', a.dl))
),
to_from as (
	select dl, len_dl, p_from, p_to from not_correct_order
), test as (
	select dl, len_dl, p_from, p_to, [p_from] as p_path, 2 as len_p_path from to_from a
	union all
	select a.dl, len_dl, b.p_from, b.p_to, arrayConcat(p_path, [b.p_from]) as p_path, len_p_path + 1 as len_p_path from test a, to_from b
	where b.dl=a.dl
	and a.p_to = b.p_from
),
test_dis as (
	select * from test
	where len_dl = len_p_path
)
select sum(p_path[(length(p_path)/2)::int+1]::int) from test_dis
