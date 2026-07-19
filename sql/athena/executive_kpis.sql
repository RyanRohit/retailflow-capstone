SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.customer_id) AS total_customers,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(AVG(oi.quantity * oi.unit_price), 2) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id;