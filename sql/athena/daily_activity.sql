SELECT
    CAST(from_iso8601_timestamp(event_time) AS DATE) AS event_date,
    COUNT(*) AS total_events
FROM clickstream
GROUP BY CAST(from_iso8601_timestamp(event_time) AS DATE)
ORDER BY event_date;