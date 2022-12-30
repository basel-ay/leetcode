# Write your MySQL query statement below

SELECT a.product_id
FROM
    Products AS a
WHERE
    a.low_fats = 'Y' AND a.recyclable = 'Y';