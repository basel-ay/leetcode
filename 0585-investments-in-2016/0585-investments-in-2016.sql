# Write your MySQL query statement below
select round(sum(tiv_2016), 2) as 'tiv_2016' from Insurance A
where exists (select * from Insurance where pid <> A.pid and tiv_2015 = A.tiv_2015)
and not exists (select * from Insurance where pid <> A.pid and (lat, lon) = (A.lat, A.lon));
