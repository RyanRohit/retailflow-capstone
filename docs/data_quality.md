# AWS Glue Data Quality

## Rules Implemented

### Completeness

- order_id
- customer_id
- order_ts

### Uniqueness

- order_id

### Referential Integrity

Validated that every `order_items.product_id` exists in `products.product_id` using a Spark left anti join.

## Outcome

The ETL validates critical business rules before writing curated data.