--day 2 part 1
--used clickhouse
with nbr_list as (
	select * from numbers(1, 10)
),
--give each line a row number and split it into an array
row_nbr AS (
		SELECT
		ROW_NUMBER() OVER (ORDER BY c1) AS rw,
		c1 AS nbr_list,
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
)
select
	level_report,
	count(*)
from levels
group by level_report
