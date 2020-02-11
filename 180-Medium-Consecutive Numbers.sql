# Write your MySQL query statement below
SELECT DISTINCT F.Num AS ConsecutiveNums
  FROM Logs AS F
       INNER JOIN Logs AS S
       ON S.Id - F.Id = 1
       INNER JOIN Logs AS T
       ON T.Id - S.Id = 1
 WHERE F.Num = S.Num
   AND S.Num = T.Num