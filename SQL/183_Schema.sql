CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customerId INTEGER,
    FOREIGN KEY (customerId) REFERENCES Customers(id)
);

DELETE FROM Customers;
DELETE FROM Orders;

INSERT INTO Customers (id, name) VALUES (1, 'Joe');
INSERT INTO Customers (id, name) VALUES (2, 'Henry');
INSERT INTO Customers (id, name) VALUES (3, 'Sam');
INSERT INTO Customers (id, name) VALUES (4, 'Max');

INSERT INTO Orders (id, customerId) VALUES (1, 3);
INSERT INTO Orders (id, customerId) VALUES (2, 1);