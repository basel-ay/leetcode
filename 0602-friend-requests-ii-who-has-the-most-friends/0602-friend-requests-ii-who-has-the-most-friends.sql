# Write your MySQL query statement below

# Check the repeated ids for both columns then detect the most friends number as below

# 1
# 1
# 2
# 2
# 3
# 3
# 3
# 4

WITH base AS (

    SELECT requester_id AS "id" FROM RequestAccepted 
    
    UNION ALL # To retain the duplicate
    
    SELECT accepter_id AS "id" FROM RequestAccepted 

)

SELECT id, COUNT(*) AS "num" FROM base
GROUP BY id
ORDER BY num DESC LIMIT 1;

