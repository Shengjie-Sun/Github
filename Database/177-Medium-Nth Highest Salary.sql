# Solution 1
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

DECLARE M INT;
SET M=N-1;

  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary
             FROM Employee
             ORDER BY Salary DESC
             LIMIT 1 OFFSET M
  );
END

# Solution 2
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT E1.salary
             FROM employee AS E1
             CROSS JOIN employee AS E2 
       WHERE E1.salary <= E2.salary
       GROUP BY E1.salary
       HAVING COUNT(DISTINCT E2.salary) = N
  );
END