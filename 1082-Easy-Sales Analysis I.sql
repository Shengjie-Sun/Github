# Write your MySQL query statement below
SELECT seller_id
  FROM Sales 
 GROUP BY seller_id
HAVING SUM(price) = (SELECT SUM(price) AS price_sum
                       FROM Sales 
                      GROUP BY seller_id
                      ORDER BY price_sum DESC
                      LIMIT 1)

/* Write your T-SQL query statement below */
SELECT TOP 1 WITH TIES seller_id
  FROM Sales
 GROUP BY seller_id
 ORDER BY SUM(price) DESC