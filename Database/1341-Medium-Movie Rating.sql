# Write your MySQL query statement below
(SELECT name AS results
  FROM Movie_Rating AS R
       INNER JOIN Users AS U
       ON R.user_id = U.user_id
 GROUP BY U.user_id
 ORDER BY COUNT(*) DESC, name ASC
 LIMIT 1)
 
 UNION ALL
 
 (SELECT title AS results
  FROM Movie_Rating AS R
       INNER JOIN Movies AS M
       ON M.movie_id = R.movie_id
 WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
 GROUP BY R.movie_id
 ORDER BY AVG(rating) DESC, title ASC
 LIMIT 1)