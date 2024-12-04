--day 2 part 2
--used clickhouse
with nbr_list as (
	select * from numbers(1, 10)
),
--give each line a row number and split it into an array
row_nbr AS (
		SELECT
		ROW_NUMBER() over () AS rw,
		--c1 AS nbr_list,
		splitByChar(' ', assumeNotNull(c1)) AS nbrs
	FROM file ('2024_day2_input.csv')
),
--here we use a number table and determine negative or positive hop from 1 number to the next in the array and also see if that hop is within the threshold
hop AS (
	SELECT 
		rw, 
		nbrs,
		multiIf(nbrs[number]::int - nbrs[number+1]::int > 0, 1, 0) AS hop_diff_pos,
		multiIf(nbrs[number]::int - nbrs[number+1]::int < 0, 1, 0) AS hop_diff_neg,
		multiIf(abs(nbrs[number]::int - nbrs[number+1]::int) BETWEEN 1 AND 3, 1, 0) AS hop_diff_ok
	FROM row_nbr a
	join nbr_list b on 0=0
	where length(a.nbrs) >= b.number + 1
),
--we agg it up and sum the arrays, checking for all positivte, all negative and if all the hops are within the threshold.
array_sum as (
	SELECT
		rw, 
		nbrs,
		arraySum(groupArray(hop_diff_pos)) as sum_hop_diff_pos,
		arraySum(groupArray(hop_diff_neg)) as sum_hop_diff_neg,
		arraySum(groupArray(hop_diff_ok)) as sum_hop_diff_ok
	FROM hop
	group by rw, nbrs
),
--then if that sum of all the hops are positive or negetive and the hop_diff, changes within the threshold, equal length of the array minus 1(number of hops) we are safe.
levels as (
select
	rw,
	nbrs,
	multiIf(
			sum_hop_diff_pos = (length(nbrs)-1) and sum_hop_diff_ok = (length(nbrs)-1), 'safe',
			sum_hop_diff_neg = (length(nbrs)-1) and sum_hop_diff_ok = (length(nbrs)-1), 'safe',
			'not_safe')  as level_report
From array_sum
),
--we then filter on only those not_safe
check_not_safe as (
	SELECT distinct
		rw, 
		nbrs,
		arrayFilter((element, index) -> index != b.number, nbrs, arrayEnumerate(nbrs)) as new_nbrs
	FROM levels a
	join nbr_list b on 0=0
	where length(a.nbrs) >= b.number
	and a.level_report = 'not_safe'
),
--we rebuild each array removing 1 item from each position to get a whole new set of arrays
hop2 AS (
	SELECT
		rw, 
		new_nbrs,
		multiIf(new_nbrs[number]::int - new_nbrs[number+1]::int > 0, 1, 0) AS hop_diff_pos,
		multiIf(new_nbrs[number]::int - new_nbrs[number+1]::int < 0, 1, 0) AS hop_diff_neg,
		multiIf(abs(new_nbrs[number]::int - new_nbrs[number+1]::int) BETWEEN 1 AND 3, 1, 0) AS hop_diff_ok
	FROM check_not_safe a
	join nbr_list b on 0=0
	where length(a.new_nbrs) >= b.number + 1
),
--redo our logic above using the new set of arrays
array_sum2 as (
	SELECT
		rw, 
		new_nbrs,
		arraySum(groupArray(hop_diff_pos)) as sum_hop_diff_pos,
		arraySum(groupArray(hop_diff_neg)) as sum_hop_diff_neg,
		arraySum(groupArray(hop_diff_ok)) as sum_hop_diff_ok
	FROM hop2
	group by rw, new_nbrs
),
--while here we will get a new set of safe levels of those not_safe but 1 was removed
levels2 as (
select
	rw,
	new_nbrs,
	multiIf(
			sum_hop_diff_pos = (length(new_nbrs)-1) and sum_hop_diff_ok = (length(new_nbrs)-1), 'safe',
			sum_hop_diff_neg = (length(new_nbrs)-1) and sum_hop_diff_ok = (length(new_nbrs)-1), 'safe',
			'not_safe')  as level_report
From array_sum2
),
levels_counts as (
	select count(distinct rw) from levels2
	where level_report = 'safe'
	union all
	select count(*) from levels
	where level_report = 'safe'
)
select sum(*) from levels_counts
