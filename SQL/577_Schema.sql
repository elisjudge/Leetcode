-- Create the Employee table
CREATE TABLE IF NOT EXISTS Employee (
    empId INTEGER,
    name TEXT,
    supervisor INTEGER,
    salary INTEGER
);

-- Create the Bonus table
CREATE TABLE IF NOT EXISTS Bonus (
    empId INTEGER,
    bonus INTEGER
);

-- Clear existing data in Employee
DELETE FROM Employee;

-- Insert data into Employee
INSERT INTO Employee (empId, name, supervisor, salary) VALUES (3, 'Brad', NULL, 4000);
INSERT INTO Employee (empId, name, supervisor, salary) VALUES (1, 'John', 3, 1000);
INSERT INTO Employee (empId, name, supervisor, salary) VALUES (2, 'Dan', 3, 2000);
INSERT INTO Employee (empId, name, supervisor, salary) VALUES (4, 'Thomas', 3, 4000);

-- Clear existing data in Bonus
DELETE FROM Bonus;

-- Insert data into Bonus
INSERT INTO Bonus (empId, bonus) VALUES (2, 500);
INSERT INTO Bonus (empId, bonus) VALUES (4, 2000);
