# Write your MySQL query statement below
SELECT EMAIL AS 'Email' 
FROM PERSON 
# The difference between the having and where clause in SQL is that the where clause cannot be used with aggregates(max, min,count,avg,sum), but the having clause can.
GROUP BY PERSON.EMAIL
HAVING COUNT(PERSON.EMAIL) >= 2;