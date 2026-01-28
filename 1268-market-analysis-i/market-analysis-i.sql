# Write your MySQL query statement below
SELECT u.user_id AS buyer_id , u.join_date,
count(order_id) AS orders_in_2019
FROM Users u LEFT JOIN Orders o ON u.user_id = o.buyer_id
AND order_date between '2019-01-01' and '2019-12-31'
GROUP BY u.user_id, u.join_date;