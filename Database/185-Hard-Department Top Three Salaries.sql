# Solution with Window Function DENSE_RANK()
WITH Salary_Rank(Name, Salary, DepartmentId, RankDense) AS
	(SELECT Name, 
	        Salary, 
					DepartmentId, 
					DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC)
		 FROM `employee-184&185`)

SELECT D.Name AS Department, 
       S.Name AS Employee, 
			 Salary 
  FROM Salary_Rank AS S
       INNER JOIN `department-184&185` AS D
       ON D.Id = S.DepartmentId 
 WHERE RankDense <= 3

 # Solution without Window Function DENSE_RANK()
SELECT
	D.NAME AS 'Department',
	E1.NAME AS 'Employee',
	E1.Salary 
FROM Employee E1
	 INNER JOIN Department AS D 
     ON E1.DepartmentId = D.Id 
WHERE 3 > (SELECT COUNT( DISTINCT E2.Salary ) 
	       FROM Employee AS E2 
           WHERE E2.Salary > E1.Salary 
	       AND E1.DepartmentId = E2.DepartmentId);