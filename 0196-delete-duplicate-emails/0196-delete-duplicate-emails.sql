# Write your MySQL query statement below
# id with the greater count should be deleted and A.email=B.email means if both the email is same.
DELETE A FROM Person AS A, Person AS B where A.id > B.id and A.email=B.email;