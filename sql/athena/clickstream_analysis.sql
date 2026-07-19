SELECT
    event_type,
    COUNT(*) AS total_events,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM clickstream
GROUP BY event_type
ORDER BY total_events DESC;