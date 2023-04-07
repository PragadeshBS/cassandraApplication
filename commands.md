# Cassandra commands to create a simple keyspace

### View keyspaces
SELECT * FROM system_schema.keyspaces;

### Create a new keyspace
CREATE KEYSPACE employee WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE employee;

### Create a table
CREATE TABLE employee_details(
    id int PRIMARY KEY,
    name text,
    city text,
    age int
);

### Insert Values
INSERT INTO employee_details(id, name, city, age) VALUES(1, 'Jack', 'Seattle', 40);
INSERT INTO employee_details(id, name, city, age) VALUES(2, 'Pragadesh', 'Chicago', 42);
INSERT INTO employee_details(id, name, city, age) VALUES(3, 'Sam', 'Washington', 34);
INSERT INTO employee_details(id, name, city, age) VALUES(4, 'Nick', 'Seattle', 42);
INSERT INTO employee_details(id, name, city, age) VALUES(5, 'Trevor', 'New York', 31);

### Fetch records
SELECT * FROM employee_details;