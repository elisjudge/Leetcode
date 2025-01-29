CREATE TABLE IF NOT EXISTS Person (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL
);

DELETE FROM Person;

INSERT INTO Person (id, email) VALUES (1, 'a@b.com');
INSERT INTO Person (id, email) VALUES (2, 'c@d.com');
INSERT INTO Person (id, email) VALUES (3, 'a@b.com');
