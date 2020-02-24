# Write your MySQL query statement below
SELECT ROUND(AVG(daily_percent)*100, 2) AS average_daily_percent FROM(
SELECT COUNT(DISTINCT R.post_id)/COUNT(DISTINCT A.post_id) AS daily_percent
  FROM Actions AS A
       LEFT JOIN Removals AS R
       ON A.post_id = R.post_id 
 WHERE extra='spam'
 GROUP BY action_date
 ORDER BY action_date) AS Daily