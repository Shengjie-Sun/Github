# Write your MySQL query statement below
SELECT DISTINCT(C1.seat_id)
  FROM cinema AS C1
       INNER JOIN cinema AS C2
       ON ABS(C1.seat_id - C2.seat_id) = 1
 WHERE C1.free = 1
   AND C2.free = 1
 ORDER BY C1.seat_id

 # Write your MySQL query statement below
SELECT C1.seat_id
  FROM cinema AS C1
       LEFT JOIN cinema AS C2
       ON C1.seat_id = C2.seat_id - 1
       LEFT JOIN cinema AS C3
       ON C1.seat_id = C3.seat_id + 1
 WHERE C1.free = 1
   AND (C2.free=1 OR C3.free=1)
 ORDER BY C1.seat_id