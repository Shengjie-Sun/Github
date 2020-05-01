/* Write your T-SQL query statement below */
WITH Groups AS 
(SELECT log_id, 
        ROW_NUMBER() OVER(ORDER BY log_id) - log_id AS groups
   FROM Logs)

SELECT MIN(log_id) AS start_id, 
       MAX(log_id) AS end_id
  FROM Groups
 GROUP BY groups
 ORDER BY MIN(log_id)
