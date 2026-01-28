# Write your MySQL query statement below
select query_name,
round(avg(rating/position),2) as quality,
round(SUM(case when rating<3 then 1 else 0 END) / count(*),4)*100 as poor_query_percentage
from queries
group by query_name;