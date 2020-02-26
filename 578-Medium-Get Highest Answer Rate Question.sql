# Write your MySQL query statement below
SELECT question_id AS survey_log
  FROM (SELECT question_id, 
               SUM(CASE WHEN action='answer' THEN 1 ELSE 0 END) / 
               SUM(CASE WHEN action='show' THEN 1 ELSE 0 END) AS rate
  FROM survey_log
 GROUP BY question_id) AS survey_rate
 ORDER BY rate DESC
 LIMIT 1

 # Write your MySQL query statement below
SELECT question_id AS 'survey_log'
  FROM survey_log
 GROUP BY question_id
 ORDER BY SUM(CASE WHEN action='answer' 
              THEN 1 ELSE 0 END) / 
          SUM(CASE WHEN action='show' 
              THEN 1 ELSE 0 END) DESC
 LIMIT 1