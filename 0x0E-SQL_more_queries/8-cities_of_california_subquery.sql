-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- Query to select cities of California using subquery
SELECT id, name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = 'California')
    ORDER BY id ASC;
