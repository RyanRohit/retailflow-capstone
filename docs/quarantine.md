# Quarantine Handling

## Objective

Invalid records should be separated from valid records before loading into the curated layer.

## Validation Performed

- Duplicate removal
- Null value checks
- Timestamp validation

## Intended Storage

Valid records:
- s3://retailflow-capstone-rohit-2026/curated/

Invalid records:
- s3://retailflow-capstone-rohit-2026/quarantine/

## Monitoring

AWS Glue logs are available in CloudWatch for monitoring ETL execution and data quality.