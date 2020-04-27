# Write your MySQL query statement below
SELECT DISTINCT E1.employee_id
  FROM Employees AS E1
       INNER JOIN Employees AS E2
       ON E1.manager_id = E2.employee_id
       INNER JOIN Employees AS E3
       ON E2.manager_id = E3.employee_id
 WHERE E1.employee_id != 1
   AND (E1.manager_id=1 OR E2.manager_id=1 or E3.manager_id=1)