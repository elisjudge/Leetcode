CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER,
    name TEXT
);

CREATE TABLE IF NOT EXISTS EmployeeUNI (
    id INTEGER,
    unique_id INTEGER
);

-- Delete all records from Employees table
DELETE FROM Employees;

-- Insert data into Employees table
INSERT INTO Employees (id, name) VALUES (1, 'Alice');
INSERT INTO Employees (id, name) VALUES (7, 'Bob');
INSERT INTO Employees (id, name) VALUES (11, 'Meir');
INSERT INTO Employees (id, name) VALUES (90, 'Winston');
INSERT INTO Employees (id, name) VALUES (3, 'Jonathan');

-- Delete all records from EmployeeUNI table
DELETE FROM EmployeeUNI;

-- Insert data into EmployeeUNI table
INSERT INTO EmployeeUNI (id, unique_id) VALUES (3, 1);
INSERT INTO EmployeeUNI (id, unique_id) VALUES (11, 2);
INSERT INTO EmployeeUNI (id, unique_id) VALUES (90, 3);
