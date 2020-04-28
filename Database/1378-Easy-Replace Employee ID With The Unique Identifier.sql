# Write your MySQL query statement below
SELECT EI.unique_id, ES.name
  FROM Employees AS ES
       LEFT JOIN EmployeeUNI AS EI
       ON ES.id = EI.id 