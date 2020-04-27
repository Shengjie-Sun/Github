SELECT A.Id AS ID 
  FROM Weather AS B
 INNER JOIN Weather AS A
 WHERE DATEDIFF(A.RecordDate, B.RecordDate)=1
   AND A.Temperature > B.Temperature

# Approach: Using JOIN and DATEDIFF()
SELECT A.Id AS ID 
  FROM Weather AS B
       INNER JOIN Weather AS A
       ON DATEDIFF(A.RecordDate, B.RecordDate)=1
       AND A.Temperature > B.Temperature