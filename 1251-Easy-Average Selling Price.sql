# Write your MySQL query statement below
SELECT P.product_id,
       ROUND(SUM(units*price) / SUM(units),2)  AS average_price
  FROM Prices AS P
       INNER JOIN UnitsSold AS U
       ON P.product_id = U.product_id
       AND purchase_date BETWEEN start_date AND end_date
 GROUP BY P.product_id