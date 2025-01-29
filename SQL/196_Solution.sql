DELETE FROM
    Person
WHERE
    id NOT IN (
    SELECT 
        MIN(id)
    FROM
        Person
    GROUP BY 
        email
);

-- -- MySQL Query

-- DELETE FROM Person
-- WHERE id NOT IN (
--     SELECT id FROM (
--         SELECT MIN(id) AS id
--         FROM Person
--         GROUP BY email
--     ) AS subquery
-- );