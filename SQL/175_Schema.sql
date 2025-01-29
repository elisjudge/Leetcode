CREATE TABLE IF NOT EXISTS Person (
    personId INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Address (
    addressId INTEGER PRIMARY KEY,
    personId INTEGER,
    city TEXT,
    state TEXT,
    FOREIGN KEY (personId) REFERENCES Person(personId)
);

DELETE FROM Person;
DELETE FROM Address;

INSERT INTO Person (personId, lastName, firstName) VALUES (1, 'Wang', 'Allen');
INSERT INTO Person (personId, lastName, firstName) VALUES (2, 'Alice', 'Bob');

INSERT INTO Address (addressId, personId, city, state) VALUES (1, 2, 'New York City', 'New York');
INSERT INTO Address (addressId, personId, city, state) VALUES (2, 3, 'Leetcode', 'California');