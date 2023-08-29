# Write your MySQL query statement below
select A.name as 'Employee', A.salary as 'Salary', B.name as 'Department' from Employee A, Department B
Where A.departmentId = B.id 
AND (departmentId, salary) 
in (SELECT departmentId, max(Salary) as max FROM Employee GROUP BY departmentId)