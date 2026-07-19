SELECT
    device,
    COUNT(*) AS total_events,
    COUNT(DISTINCT customer_id) AS unique_users
FROM clickstream
GROUP BY device
ORDER BY total_events DESC;