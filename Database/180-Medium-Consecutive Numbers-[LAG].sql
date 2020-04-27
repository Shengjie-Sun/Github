# Write your MySQL query statement below
SELECT DISTINCT F.Num AS ConsecutiveNums
  FROM Logs AS F
       INNER JOIN Logs AS S
       ON S.Id - F.Id = 1
       INNER JOIN Logs AS T
       ON T.Id - S.Id = 1
 WHERE F.Num = S.Num
   AND S.Num = T.Num

/* Write your T-SQL query statement below */
SELECT DISTINCT Num AS ConsecutiveNums
  FROM (SELECT Id, 
               Num, 
               LAG(NUM, 1) OVER(ORDER BY Id) AS P, 
               LEAD(NUM, 1) OVER(ORDER BY Id) AS N 
        FROM Logs) AS Sub
 WHERE Num = P AND Num = N