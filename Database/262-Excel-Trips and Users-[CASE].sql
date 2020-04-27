# Write your MySQL query statement below
SELECT Request_at AS Day,
       ROUND(SUM(CASE WHEN Status='completed' THEN 0 ELSE 1 END)/COUNT(*),2) AS Cancellation_Rate 
  FROM (SELECT Client_Id, Driver_Id, Status, Request_at 
          FROM trips AS T
               INNER JOIN users AS C 
			   ON T.Client_Id = C.Users_Id
			   INNER JOIN users AS D
			   ON T.Client_Id = D.Users_Id 
               WHERE C.Banned = 'No' 
               AND D.Banned = 'No' 
               AND T.Request_at BETWEEN '2013-10-01' AND '2013-10-03') AS Ban
 GROUP BY Request_at;


 WITH `banned-262` ( Client_Id, Driver_Id, STATUS, Request_at, Banned ) AS (
	SELECT
		Client_Id,
		Driver_Id,
		STATUS,
		Request_at,
		C.Banned 
	FROM
		`trips-262` AS T
		INNER JOIN `users-262` AS C ON T.Client_Id = C.Users_Id
		INNER JOIN `users-262` AS D ON T.Client_Id = D.Users_Id 
	WHERE
		C.Banned = 'No' 
		AND D.Banned = 'No' 
	) SELECT
	Request_at AS DAY,
	ROUND( SUM( CASE WHEN STATUS = 'completed' THEN 0 ELSE 1 END )/ COUNT(*), 2 ) AS Cancellation_Rate 
FROM
	`banned-262` 
GROUP BY
	Request_at;