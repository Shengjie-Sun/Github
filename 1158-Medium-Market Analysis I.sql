# Write your MySQL query statement below
SELECT user_id AS buyer_id, join_date, 
       # 注意此处使用COUNT(order_date)和COUNT(*)的区别
       IFNULL(COUNT(order_date), 0) AS orders_in_2019
  FROM Users AS U
       # 注意此处必须使用LEFT JOIN
       LEFT JOIN Orders AS O
       ON U.user_id = O.buyer_id
       # 注意此处的年份筛选需要放在ON下
       AND YEAR(order_date) = '2019'
 GROUP BY user_id
 ORDER BY user_id