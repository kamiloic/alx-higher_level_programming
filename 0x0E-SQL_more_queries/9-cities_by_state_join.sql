-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- Query to list all cities with their respective states
SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
