# Write your MySQL query statement below

/*
-- average exp years per project (groub by)
-- inner join the two tables to get the project_id and experience_years columns
-- round the results to 2 digits
*/

SELECT project_id, ROUND(AVG(experience_years), 2) AS 'average_years'
FROM Project AS p
INNER JOIN Employee AS e
ON p.employee_id = e.employee_id
GROUP BY 1