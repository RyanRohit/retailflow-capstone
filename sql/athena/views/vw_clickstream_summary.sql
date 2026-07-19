CREATE OR REPLACE VIEW vw_clickstream_summary AS
SELECT
    customer_id,
    CAST(from_iso8601_timestamp(event_time) AS DATE) AS event_date,
    event_type,
    page,
    device,
    browser
FROM clickstream;