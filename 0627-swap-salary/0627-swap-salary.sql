# Write your MySQL query statement below

/*
-- Detect 'f' and 'm' values
-- Using update clause to change the values without using any select statement
*/

UPDATE Salary
SET sex =
    CASE
        WHEN sex = 'f' THEN 'm'
        WHEN sex = 'm' THEN 'f'
        ELSE sex
    END;