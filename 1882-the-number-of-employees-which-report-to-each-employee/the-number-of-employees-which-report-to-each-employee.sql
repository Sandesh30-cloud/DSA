# Write your MySQL query statement below
select 
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
from employees e
join employees m
    on e.reports_to = m.employee_id
group by m.employee_id, m.name
order by m.employee_id;