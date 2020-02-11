SELECT
	id,
	MAX( CASE WHEN MONTH = 'Jan' THEN revenue ELSE NULL END ) AS Jan_Revenue,
	MAX( CASE WHEN MONTH = 'Feb' THEN revenue ELSE NULL END ) AS Feb_Revenue,
	MAX( CASE WHEN MONTH = 'Mar' THEN revenue ELSE NULL END ) AS Mar_Revenue,
	MAX( CASE WHEN MONTH = 'Apr' THEN revenue ELSE NULL END ) AS Apr_Revenue,
	MAX( CASE WHEN MONTH = 'May' THEN revenue ELSE NULL END ) AS May_Revenue,
	MAX( CASE WHEN MONTH = 'Jun' THEN revenue ELSE NULL END ) AS Jun_Revenue,
	MAX( CASE WHEN MONTH = 'Jul' THEN revenue ELSE NULL END ) AS Jul_Revenue,
	MAX( CASE WHEN MONTH = 'Aug' THEN revenue ELSE NULL END ) AS Aug_Revenue,
	MAX( CASE WHEN MONTH = 'Sep' THEN revenue ELSE NULL END ) AS Sep_Revenue,
	MAX( CASE WHEN MONTH = 'Oct' THEN revenue ELSE NULL END ) AS Oct_Revenue,
	MAX( CASE WHEN MONTH = 'Nov' THEN revenue ELSE NULL END ) AS Nov_Revenue,
	MAX( CASE WHEN MONTH = 'Dec' THEN revenue ELSE NULL END ) AS Dec_Revenue 
FROM
	Department 
GROUP BY
	id 
ORDER BY
	id