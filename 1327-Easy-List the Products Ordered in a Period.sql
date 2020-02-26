# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
  FROM Orders AS O
       INNER JOIN Products AS P
       ON O.product_id = P.product_id
 WHERE MONTH(order_date)='2'
 GROUP BY P.product_id
HAVING SUM(unit)>=100