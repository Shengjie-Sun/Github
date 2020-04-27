# Write your MySQL query statement below
SELECT country_name,
       (CASE WHEN AVG(weather_state)<=15 THEN 'Cold'
             WHEN AVG(weather_state)>=25 THEN 'Hot'
             ELSE 'Warm'
        END) AS weather_type
  FROM Countries AS C
       INNER JOIN Weather AS W
       ON C.country_id = W.country_id
 WHERE MONTH(day)='11'
 GROUP BY country_name