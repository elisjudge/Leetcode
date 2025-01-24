CREATE TABLE IF NOT EXISTS Visits (
    visit_id INTEGER,
    customer_id INTEGER
);

CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER,
    visit_id INTEGER,
    amount INTEGER
);

DELETE FROM Visits;

INSERT INTO Visits (visit_id, customer_id)
VALUES
    (1, 23),
    (2, 9),
    (4, 30),
    (5, 54),
    (6, 96),
    (7, 54),
    (8, 54);

DELETE FROM Transactions;

INSERT INTO Transactions (transaction_id, visit_id, amount)
VALUES
    (2, 5, 310),
    (3, 5, 300),
    (9, 5, 200),
    (12, 1, 910),
    (13, 2, 970);