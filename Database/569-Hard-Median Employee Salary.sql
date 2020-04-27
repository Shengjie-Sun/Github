/* Write your T-SQL query statement below */
WITH
  Employee_Order AS(
SELECT *,
       ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary DESC, Id DESC) AS rdesc,
       ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary ASC, Id ASC) AS rasc
  FROM Employee)
  
SELECT Id, Company,Salary
FROM Employee_Order
WHERE ABS(rdesc-rasc) <= 1