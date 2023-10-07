# Write your MySQL query statement below
# SELECT product_id, year AS first_year, quantity, price from Sales 
# WHERE (product_id, year) IN (

# SELECT product_id, MIN(year) FROM Sales
# GROUP BY product_id
    
# )


SELECT product_id, year AS first_year, quantity, price from (

SELECT *, RANK() OVER(PARTItiON BY product_id ORDER By year) as rnk FROM Sales
    
) AS rnk_tbl

WHERE rnk = 1;

