# Solution 1
# Write your MySQL query statement below
SELECT customer_id, customer_name FROM(
SELECT O.customer_id, customer_name, GROUP_CONCAT(product_name) AS product_name
  FROM Orders AS O
       LEFT JOIN Customers AS C
       ON O.customer_id = C.customer_id
 GROUP BY customer_id) AS Products
 WHERE product_name LIKE '%A%' AND product_name LIKE '%B%' AND product_name NOT LIKE '%C%'

# Solution 2
# Write your MySQL query statement below
SELECT O.customer_id, 
       C.customer_name
  FROM Orders AS O
       LEFT JOIN Customers AS C
       ON O.customer_id = C.customer_id
 GROUP BY O.customer_id
HAVING SUM(O.product_name = 'A') AND SUM(O.product_name = 'B') AND NOT SUM(O.product_name = 'C')