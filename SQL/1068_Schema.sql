CREATE TABLE IF NOT EXISTS Sales (
    sale_id INTEGER,
    product_id INTEGER,
    year INTEGER,
    quantity INTEGER,
    price INTEGER
);

CREATE TABLE IF NOT EXISTS Product (
    product_id INTEGER,
    product_name TEXT
);

DELETE FROM Sales;

INSERT INTO Sales (sale_id, product_id, year, quantity, price)
VALUES
    (1, 100, 2008, 10, 5000),
    (2, 100, 2009, 12, 5000),
    (7, 200, 2011, 15, 9000);

DELETE FROM Product;

INSERT INTO Product (product_id, product_name)
VALUES
    (100, 'Nokia'),
    (200, 'Apple'),
    (300, 'Samsung');