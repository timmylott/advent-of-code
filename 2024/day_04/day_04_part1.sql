--day 4 part 1
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
vert_pov as (
	select
		pos,
		arrayStringConcat(groupArray(letter)) as pov_ln
	from 
	(select * from split_ln
		order by pos, row_nbr)
	group by pos
),
vert as (
	select
		arrayJoin(extractAll(pov_ln, 'XMAS')) as extracted
	From vert_pov
	UNION ALL
	select
		arrayJoin(extractAll(pov_ln, 'SAMX')) as extracted
	From vert_pov
),
horz as (
	select
		arrayJoin(extractAll(dl, 'XMAS')) as extracted
	From ld
	union all
	select
		arrayJoin(extractAll(dl, 'SAMX')) as extracted
	From ld
),
--rotate cube to right and rebuilt lines to check diagonal
max_row as (
	select max(row_nbr) as max_row_nbr from split_ln
),
new_row_number as (
select
	*,
	case
		when row_nbr=max_row_nbr and pos > 1 then row_nbr + (pos-1)
		else
			row_nbr + (pos -  1) end as new_row_nbr
From split_ln one
join max_row on 0=0
),
new_pos_number as (
select
*,
	case
		when row_nbr=max_row_nbr and pos > 1 then pos - (new_row_nbr - row_nbr)
		when new_row_nbr>max_row_nbr then pos-(new_row_nbr-max_row_nbr)
	else
		pos+(1-1) end as new_pos
From new_row_number
),
new_nbr_order as (
	select * From new_pos_number
	order by new_row_nbr, new_pos
),
diagonal as (
	select new_row_nbr as row_nbr, arrayStringConcat(groupArray(letter)) as pov_ln
	from new_nbr_order
	group by new_row_nbr
),
diag_1 as (
	select
		arrayJoin(extractAll(pov_ln, 'XMAS')) as extracted
	From diagonal
	union all
	select
		arrayJoin(extractAll(pov_ln, 'SAMX'))as extracted
	From diagonal
),
--rotate the other way to get the opposite diagonal
max_row_2 as (
	select max(row_nbr) as max_row_nbr from split_ln
),
new_row_number_2 as (
select
	*,
	row_nbr + (max_row_nbr-pos) as new_row_nbr
From split_ln one
join max_row_2 on 0=0
),
new_pos_number_2 as (
select
*,
 case when new_row_nbr > max_row_nbr then pos-(1-1)
 else pos-(pos-row_nbr) end as new_pos
From new_row_number_2
),
new_nbr_order_2 as (
	select * From new_pos_number_2
	order by new_row_nbr, new_pos
),
diagonal_2 as (
select new_row_nbr as row_nbr, arrayStringConcat(groupArray(letter)) as pov_ln
from new_nbr_order_2
group by new_row_nbr
),
diag_2 as (
	select
		arrayJoin(extractAll(pov_ln, 'XMAS')) as extracted
	From diagonal_2
	union all
	select
		arrayJoin(extractAll(pov_ln, 'SAMX'))as extracted
	From diagonal_2
),
final as (
	select 'vert', count(*) as cnt From vert
	union all
	select 'horz', count(*) as cnt From horz
	union all
	select 'diag_1', count(*) as cnt from diag_1
	union all
	select 'diag_2', count(*) as cnt from diag_2
)
select sum(cnt) from final
