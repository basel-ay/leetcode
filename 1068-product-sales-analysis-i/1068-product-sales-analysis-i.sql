# Write your MySQL query statement below
SELECT S.year, S.price, P.product_name FROM Sales S 
INNER JOIN Product P
ON S.product_id = P.product_id;