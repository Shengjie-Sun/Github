# Write your MySQL query statement below
SELECT B.book_id, name
  FROM Books AS B
       LEFT JOIN Orders AS O
       ON O.book_id = B.book_id 
       AND dispatch_date >= '2018-06-23' 
 WHERE available_from < '2019-05-23'
 GROUP BY B.book_id
HAVING IFNULL(SUM(quantity),0)<10