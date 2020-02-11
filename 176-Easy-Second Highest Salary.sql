# Solution 1 with Sub Query
SELECT MAX(Salary) AS SecondHighestSalary 
  FROM Employee
 WHERE Salary < 
    (SELECT MAX(Salary) 
       FROM Employee);

# Solution 2 
SELECT DISTINCT Salary AS SecondHighestSalary
  FROM Employee
 ORDER BY Salary DESC
 LIMIT 1 OFFSET 1;