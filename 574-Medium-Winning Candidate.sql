# Write your MySQL query statement below
SELECT C.Name
  FROM Candidate AS C
       INNER JOIN Vote AS V
       ON V.CandidateID = C.id
 GROUP BY Name
 ORDER BY COUNT(*) DESC
 LIMIT 1