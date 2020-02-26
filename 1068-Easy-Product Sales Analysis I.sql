# Write your MySQL query statement below
SELECT product_name, year, price
  FROM Product AS P
       INNER JOIN Sales AS S
       ON P.product_id = S.product_id