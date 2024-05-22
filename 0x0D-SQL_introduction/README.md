# SQL Introduction

This repository contains a series of SQL scripts aimed at introducing various SQL concepts and operations. Below is a summary of each task and its purpose:

## Basic Tasks

### Task 0: Create a Database
**Filename:** `0-create_database.sql`

This script creates the `hbtn_0c_0` database if it does not already exist in the MySQL server.

### Task 1: List Databases
**Filename:** `1-list_databases.sql`

This script lists all databases on the MySQL server.

### Task 2: Delete a Database
**Filename:** `2-remove_database.sql`

This script deletes the `hbtn_0c_0` database if it exists in the MySQL server.

### Task 3: List Tables
**Filename:** `3-list_tables.sql`

This script lists all tables of a database passed as an argument in the MySQL server.

### Task 4: First Table
**Filename:** `4-first_table.sql`

This script creates a table called `first_table` with specific fields in the current database.

### Task 5: Full Description
**Filename:** `5-full_table.sql`

This script prints the full description of the `first_table` from the `hbtn_0c_0` database.

### Task 6: List All in Table
**Filename:** `6-list_values.sql`

This script lists all rows of the `first_table` from the `hbtn_0c_0` database.

### Task 7: First Add
**Filename:** `7-insert_value.sql`

This script inserts a new row into the `first_table` in the `hbtn_0c_0` database.

### Task 8: Count 89
**Filename:** `8-count_89.sql`

This script displays the number of records with id = 89 in the `first_table` of the `hbtn_0c_0` database.

## Advanced Tasks

### Task 17: Go to UTF8
**Filename:** `100-move_to_utf8.sql` (Advanced)

This script converts the `hbtn_0c_0` database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) along with the `first_table` table and the `name` field in the `first_table`.

### Task 18: Temperatures #0
**Filename:** `101-avg_temperatures.sql` (Advanced)

This script calculates and displays the average temperature (Fahrenheit) by city ordered by temperature (descending) from a table named `temperatures` in the `hbtn_0c_0` database.

### Task 19: Temperatures #1
**Filename:** `102-top_city.sql` (Advanced)

This script calculates and displays the top 3 cities' temperatures during July and August ordered by temperature (descending) from a table named `temperatures` in the `hbtn_0c_0` database.

### Task 20: Temperatures #2
**Filename:** `103-max_state.sql` (Advanced)

This script calculates and displays the maximum temperature of each state ordered by state name from a table named `temperatures` in the `hbtn_0c_0` database.

---

## Author
- **Loïc Kami**
  - Email: loic@lkami.pro
  - LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/kamiloic)
  - GitHub: [GitHub Profile](https://github.com/kamiloic)
