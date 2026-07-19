SELECT
    page,
    COUNT(*) AS page_views
FROM clickstream
GROUP BY page
ORDER BY page_views DESC;