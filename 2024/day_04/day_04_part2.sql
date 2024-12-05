--day 4 part 2
--used clickhouse
with nbr_list as (
	select * from numbers(1, 200)
),
ld as (
	SELECT
		row_number() over () as row_nbr,
		*
	FROM file ('adoc/2024_day4_input.txt', 'TSV', 'dl String')
),
split_ln as (
	select
		row_nbr, 
		number as pos, 
		substr(dl, number, 1) as letter
	From ld
	join nbr_list on 0=0
	where number <= length(dl)
),
all_a as (
select * from split_ln
where letter = 'A'
)
select count(*) from all_a aa
join split_ln a on a.row_nbr::Int64 = (aa.row_nbr - 1) and a.pos::Int64 = (aa.pos - 1) and a.letter in ('M','S')
join split_ln b on b.row_nbr = (aa.row_nbr + 1) and b.pos = (aa.pos + 1) and b.letter in ('M','S')
join split_ln c on c.row_nbr::Int64 = (aa.row_nbr - 1) and c.pos = (aa.pos + 1) and c.letter in ('M','S')
join split_ln d on d.row_nbr = (aa.row_nbr + 1) and d.pos::Int64 = (aa.pos - 1) and d.letter in ('M','S')
where
	a.letter <> b.letter
	and c.letter <> d.letter