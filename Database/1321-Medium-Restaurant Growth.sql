/* Write your T-SQL query statement below */
WITH Amount AS(
SELECT visited_on, 
       SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS 6 PRECEDING) AS amount,
       ROUND(AVG(SUM(amount)*1.0) OVER(ORDER BY visited_on ROWS 6 PRECEDING),2) AS average_amount
  FROM Customer
 GROUP BY visited_on)

 SELECT * FROM Amount
  WHERE DATEDIFF(DAY, (SELECT MIN(visited_on) FROM Amount), visited_on)>=6