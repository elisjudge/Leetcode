SELECT 
    p.project_id,
    ROUND((SUM(e.experience_years) * 1.00 / COUNT(p.employee_id)),2) AS average_years
FROM 
    Project AS p
    JOIN
        Employee AS e ON p.employee_id = e.employee_id
GROUP BY
    p.project_id;
