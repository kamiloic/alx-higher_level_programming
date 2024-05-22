-- List the number of records with the same score in the table second_table ordered by score (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
