CREATE TABLE IF NOT EXISTS Weather (
    id INTEGER,
    recordDate DATE,
    temperature INTEGER
);

DELETE FROM Weather;

INSERT INTO Weather (id, recordDate, temperature) VALUES 
('1', '2015-01-01', '10'),
('2', '2015-01-02', '25'),
('3', '2015-01-03', '20'),
('4', '2015-01-04', '30');
