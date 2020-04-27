/* Write your T-SQL query statement below */
WITH 
     TRUST (user_id, trusted_contacts_cnt) 
  AS 
     (SELECT user_id, COUNT(email)
        FROM Contacts AS CO
             INNER JOIN Customers AS CU
             ON CO.contact_name=CU.customer_name
       GROUP BY user_id),
       
     CONTACT (user_id, contacts_cnt) 
  AS 
     (SELECT user_id, COUNT(contact_name)
        FROM Contacts
       GROUP BY user_id)

SELECT invoice_id, customer_name, price, 
       ISNULL(contacts_cnt,0) AS contacts_cnt, 
       ISNULL(trusted_contacts_cnt,0) AS trusted_contacts_cnt
  FROM Invoices AS I
       LEFT JOIN CONTACT AS CO
       ON I.user_id=CO.user_id
       LEFT JOIN TRUST AS TR
       ON I.user_id=TR.user_id
       LEFT JOIN Customers AS CU
       ON I.user_id=CU.customer_id
 ORDER BY invoice_id