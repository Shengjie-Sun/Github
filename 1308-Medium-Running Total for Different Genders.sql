/* Write your T-SQL query statement below */
SELECT gender, day, 
       SUM(score_points) OVER(PARTITION BY gender ORDER BY day) AS total
  FROM Scores
 ORDER BY gender, day

 # Write your MySQL query statement below
SELECT S1.gender, S1.day,
       # 注意聚合的对象
       SUM(S2.score_points) AS total
  FROM Scores AS S1
       INNER JOIN Scores AS S2
       ON S1.gender = S2.gender AND S1.day>=S2.day
 GROUP BY S1.gender, S1.day
 ORDER BY S1.gender, S1.day