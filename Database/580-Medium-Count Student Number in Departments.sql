# Write your MySQL query statement below
SELECT dept_name, IFNULL(COUNT(student_id),0) AS student_number
  FROM department AS D
       LEFT JOIN student AS S
       ON D.dept_id = S.dept_id
 GROUP BY dept_name
 ORDER BY student_number DESC, dept_name ASC