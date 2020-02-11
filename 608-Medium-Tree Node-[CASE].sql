# Write your MySQL query statement below
SELECT DISTINCT T1.id,
       (CASE WHEN T1.p_id IS NULL THEN "Root"
             WHEN T2.id IS NULL THEN "Leaf"
             ELSE "Inner"
        END) AS Type
  FROM tree AS T1
       LEFT JOIN tree AS T2
       ON T2.p_id = T1.id

            
            
