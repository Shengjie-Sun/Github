# Write your MySQL query statement below

SELECT id, COUNT(nums) AS num
  FROM
       (SELECT requester_id AS id, requester_id AS nums
          FROM request_accepted
         UNION ALL
        SELECT accepter_id AS id, accepter_id AS nums
          FROM request_accepted) AS friends
 GROUP BY id
 ORDER BY num DESC
 LIMIT 1