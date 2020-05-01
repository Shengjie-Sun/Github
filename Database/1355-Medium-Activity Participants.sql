/* Write your T-SQL query statement below */
WITH People AS (SELECT activity, COUNT(name) AS people
  FROM Friends
 GROUP BY activity) 

 SELECT activity FROM People
  WHERE people>(SELECT MIN(people) FROM People)
    AND people<(SELECT MAX(people) FROM People)