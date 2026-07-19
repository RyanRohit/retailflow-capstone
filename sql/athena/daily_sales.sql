SELECT
    CAST(from_iso8601_timestamp(order_ts) AS DATE) AS order_date,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY CAST(from_iso8601_timestamp(order_ts) AS DATE)
ORDER BY order_date;