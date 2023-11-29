# Write your MySQL query statement below

/*
-- Select actor_id, director_id columns
-- Group by actor_id, director_id to find how many times they cooperated
-- Show only at least three times (>=)
*/

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING count(*) >= 3