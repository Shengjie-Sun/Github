/* Write your T-SQL query statement below */
WITH 
America AS
     (SELECT name, ROW_NUMBER() OVER(ORDER BY name) AS Id
		  FROM student
			WHERE continent = 'America'),
Asia AS
     (SELECT name, ROW_NUMBER() OVER(ORDER BY name) AS Id
		  FROM student
			WHERE continent = 'Asia'),
Europe AS
     (SELECT name, ROW_NUMBER() OVER(ORDER BY name) AS Id
		  FROM student
			WHERE continent = 'Europe')

SELECT AME.name AS America, 
       ASI.name AS Asia,
			 EUR.name AS Europe
  FROM America AS AME
       LEFT JOIN Asia AS ASI
			 ON AME.Id = ASI.Id
			 LEFT JOIN Europe AS EUR
			 ON AME.Id = EUR.Id

/* Write your T-SQL query statement below */ 
SELECT
  MIN( CASE WHEN continent = 'America' THEN NAME ELSE NULL END ) AS America,
  MIN( CASE WHEN continent = 'Asia' THEN NAME ELSE NULL END ) AS Asia,
  MIN( CASE WHEN continent = 'Europe' THEN NAME ELSE NULL END ) AS Europe 
FROM
	( SELECT *, ROW_NUMBER() OVER ( PARTITION BY continent ORDER BY NAME ) AS rnk FROM student ) AS student_order 
GROUP BY
  rnk