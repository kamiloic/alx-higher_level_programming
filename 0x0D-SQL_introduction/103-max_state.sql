SELECT state, MAX(temp_fahrenheit) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
