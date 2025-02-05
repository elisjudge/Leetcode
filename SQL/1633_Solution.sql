SELECT
    r.contest_id,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Users) ,2)  AS percentage
FROM
    Register as r
    JOIN
        Users as u ON r.user_id = u.user_id

GROUP BY
    r.contest_id

ORDER BY
    percentage DESC,
    r.contest_id ASC;