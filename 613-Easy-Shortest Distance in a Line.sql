# Write your MySQL query statement below
SELECT MIN(ABS(P1.x-p2.x)) AS shortest
  FROM point AS P1
       CROSS JOIN point AS P2
 ON P1.x != P2.x