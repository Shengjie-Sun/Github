# Write your MySQL query statement below
SELECT T1.follower AS follower, 
       COUNT(DISTINCT T2.follower) AS num
  FROM follow AS T1
       LEFT JOIN follow AS T2
       ON T1.follower = T2.followee
 GROUP BY T1.follower
HAVING num > 0

# Write your MySQL query statement below
SELECT followee AS follower, 
       COUNT(DISTINCT follower) AS num
  FROM follow
 WHERE followee IN (SELECT follower FROM follow)
 GROUP BY followee
 ORDER BY followee; 