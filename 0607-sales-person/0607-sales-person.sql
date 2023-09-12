# Write your MySQL query statement below
select S.name from SalesPerson S
where S.name not in (select S.name from SalesPerson S
left join Orders O on S.sales_id = O.sales_id
left join Company C on C.com_id = O.com_id
where C.name = 'RED')
