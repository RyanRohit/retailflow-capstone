CREATE OR REPLACE VIEW vw_sales_summary AS
SELECT
    o.order_id,
    CAST(from_iso8601_timestamp(o.order_ts) AS DATE) AS order_date,
    o.customer_id,
    c.first_name,
    c.last_name,
    o.store_region,
    o.status,
    oi.product_id,
    p.product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS sales_amount
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id;