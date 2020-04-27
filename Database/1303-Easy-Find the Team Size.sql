/* Write your T-SQL query statement below */
SELECT employee_id,
       COUNT(*) OVER(PARTITION BY team_id) AS team_size
  FROM Employee
 ORDER BY employee_id

 # Write your MySQL query statement below
SELECT E1.employee_id, E2.team_size
  FROM Employee AS E1
       INNER JOIN (SELECT team_id, COUNT(*) AS team_size
                   FROM Employee 
                   GROUP BY team_id) AS E2
       ON E1.team_id = E2.team_id