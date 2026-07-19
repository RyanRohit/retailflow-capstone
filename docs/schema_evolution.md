# Schema Evolution

## Objective

Support schema evolution when new columns are introduced in incoming JSON files without breaking existing data.

## Scenario

Day 2 introduced a new field:

- `discount_code`

Day 1 records do not contain this column.

## Implementation

The ETL reads JSON files using Spark schema inference and writes Parquet with schema merge enabled:

```python
orders_df.write \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .parquet(CURATED_PATH + "orders/")
```

## Result

- Existing Day 1 records remain valid.
- `discount_code` is populated for Day 2 records.
- Day 1 records contain `NULL` for the new column.