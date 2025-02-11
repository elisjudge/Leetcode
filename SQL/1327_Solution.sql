SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM
    Orders AS o
    LEFT JOIN
        Products AS p 
        ON o.product_id = p.product_id
WHERE
    o.order_date >= '2020-02-01' AND o.order_date <= '2020-02-29'
GROUP BY
    p.product_name
HAVING
    SUM(o.unit) >= 100;
