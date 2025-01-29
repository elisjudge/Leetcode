CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL,
    managerId INTEGER,
    FOREIGN KEY (managerId) REFERENCES Employee(id)
);

DELETE FROM Employee;

-- Insert data into the Employee table
INSERT INTO Employee (id, name, salary, managerId) VALUES (1, 'Joe', 70000, 3);
INSERT INTO Employee (id, name, salary, managerId) VALUES (2, 'Henry', 80000, 4);
INSERT INTO Employee (id, name, salary, managerId) VALUES (3, 'Sam', 60000, NULL);
INSERT INTO Employee (id, name, salary, managerId) VALUES (4, 'Max', 90000, NULL);
