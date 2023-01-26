# Write your MySQL query statement below
SELECT CUSTOMER.NAME AS 'name'
FROM CUSTOMER
WHERE (CUSTOMER.referee_id <> 2 OR CUSTOMER.referee_id IS NULL)