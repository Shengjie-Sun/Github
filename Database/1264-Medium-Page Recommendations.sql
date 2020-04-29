# Write your MySQL query statement below
SELECT DISTINCT page_id AS recommended_page
  FROM (SELECT (CASE WHEN user1_id = 1 THEN user2_id 
                     WHEN user2_id = 1 THEN user1_id 
                ELSE NULL
                END) AS friends_id
          FROM Friendship
        ) AS F
       LEFT JOIN Likes AS L
       ON F.friends_id = L.user_id
 WHERE page_id NOT IN (SELECT page_id FROM Likes WHERE user_id=1)
   AND page_id IS NOT NULL