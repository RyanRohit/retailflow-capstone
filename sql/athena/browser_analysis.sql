SELECT
    browser,
    COUNT(*) AS total_events
FROM clickstream
GROUP BY browser
ORDER BY total_events DESC;