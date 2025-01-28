SELECT
    machine_id,
    ROUND(AVG(process_time), 3) AS processing_time
FROM (
    SELECT
        a.machine_id,
        a.process_id,
        b.timestamp - a.timestamp AS process_time 
    FROM
        Activity AS a
        JOIN
            Activity AS b 
            ON a.machine_id = b.machine_id 
            AND a.process_id = b.process_id
    WHERE
        a.activity_type = 'start'
        AND b.activity_type = 'end'
) AS process_data
GROUP BY
    machine_id;
