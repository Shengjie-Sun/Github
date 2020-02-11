# Write your MySQL query statement below
SELECT E.Name AS Employee
  FROM Employee AS E
       INNER JOIN Employee AS M
       ON E.ManagerId = M.Id
 WHERE E.Salary > M.Salary