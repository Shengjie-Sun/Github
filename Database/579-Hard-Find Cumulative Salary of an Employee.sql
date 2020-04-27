# Write your MySQL query statement below
SELECT
	Id,
	Month,
	SUM( Salary ) OVER ( PARTITION BY Id ORDER BY Month ROWS 2 PRECEDING ) AS Salary 
FROM
	`employee-579` 
WHERE
	( Id, Month ) NOT IN ( SELECT Id, MAX( Month ) FROM `employee-579` GROUP BY Id ) 
ORDER BY
	Id ASC, Month DESC

