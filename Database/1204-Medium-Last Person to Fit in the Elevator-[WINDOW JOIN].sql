/* Write your T-SQL query statement below */

/* SQL Server 中不能实用LIMIT */
SELECT TOP 1 person_name 
  FROM 
       (SELECT *, SUM(weight) OVER(ORDER BY turn) AS weight_sum
          FROM Queue) AS weight
 WHERE weight_sum <= 1000
 ORDER BY turn DESC

 # Write your MySQL query statement below
SELECT Q.person_name
  FROM Queue AS Q
       INNER JOIN Queue AS F
       # 注意这里的条件是大于等于
       ON Q.turn >= F.turn
 GROUP BY Q.person_id
HAVING SUM(F.weight) <= 1000
 ORDER BY Q.turn DESC
 # 用这个来取最大的数据
 LIMIT 1