# Write your MySQL query statement below
SELECT product_id, 
       year AS first_year,
       quantity,
       price
  FROM Sales
 WHERE (product_id, year)
        # 使用聚合函数时，SELECT 子句中的元素有严格的限制
    IN (SELECT product_id, MIN(year) AS year
          FROM Sales
         GROUP BY product_id)