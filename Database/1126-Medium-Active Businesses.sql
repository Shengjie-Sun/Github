# Write your MySQL query statement below
SELECT business_id
  FROM Events AS E
       INNER JOIN (SELECT event_type, AVG(occurences) AS occurences_avg
                   FROM Events
                   GROUP BY event_type) AS A
       ON E.event_type = A.event_type
 GROUP BY business_id
HAVING SUM(CASE WHEN E.occurences > A.occurences_avg THEN 1 ELSE 0 END)>=2

# Write your MySQL query statement below
SELECT business_id
  FROM Events AS E
       INNER JOIN (SELECT event_type, AVG(occurences) AS occurences_avg
                   FROM Events
                   GROUP BY event_type) AS A
       ON E.event_type = A.event_type
 WHERE E.occurences > A.occurences_avg
 GROUP BY business_id
HAVING COUNT(*)>=2