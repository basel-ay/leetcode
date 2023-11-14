# Write your MySQL query statement below

/*

- Detect the biggest unique number
- Print null if there isn't any unique values

*/

SELECT
  CASE
      WHEN COUNT(num) = 1 THEN num
      ELSE NULL
  END AS 'num'
FROM MyNumbers
GROUP BY num
ORDER BY num DESC LIMIT 1; 