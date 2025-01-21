-- Create table
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    low_fats TEXT CHECK(low_fats IN ('Y', 'N')),
    recyclable TEXT CHECK(recyclable IN ('Y', 'N'))
);

-- Clear existing data in the table
DELETE FROM Products;

-- Insert sample data
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (0, 'Y', 'N');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (1, 'Y', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (2, 'N', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (3, 'Y', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (4, 'N', 'N');
