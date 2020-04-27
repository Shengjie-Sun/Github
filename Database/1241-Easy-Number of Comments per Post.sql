# Write your MySQL query statement below
SELECT post_id, 
       COUNT(DISTINCT sub_id) AS number_of_comments
  FROM 
       (SELECT sub_id AS post_id
        FROM Submissions
        WHERE parent_id IS NULL) AS P
  LEFT JOIN Submissions AS S
    ON P.post_id = S.parent_id
 GROUP BY post_id