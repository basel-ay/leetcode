# Write your MySQL query statement below

# This problem involves switching students' seats in a classroom based on their id. If the id is even, the student should move to the seat of id-1. If it is odd, they should move to id+1, unless it's the last id (in which case, they stay in their current seat because there's no seat with id+1).

SELECT

CASE  
        # Even id
        WHEN id % 2 = 0 THEN id - 1 
        # Odd id, also notice that the last row has the number 5 but if we do not include this condition, row 5 will turn to row 6
        WHEN id % 2 <> 0 AND id < (SELECT COUNT(*) FROM Seat) THEN id + 1
        ELSE id
    
END AS id, student 

FROM Seat ORDER BY id;