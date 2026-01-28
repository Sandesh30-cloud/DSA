# Write your MySQL query statement below
select
    'Low Salary' As category
    ,count(case when income<20000 then 1 END) AS accounts_count
from accounts

union all

select
    'Average Salary' AS category
    ,count(case when income between 20000 and 50000 then 1 END) AS accounts_count
from accounts

UNION ALL

SELECT 
    'High Salary' AS category
    ,COUNT(CASE WHEN income>50000 THEN 1 END) AS accounts_count
FROM accounts