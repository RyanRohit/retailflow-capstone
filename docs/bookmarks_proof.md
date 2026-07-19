# Glue Job Bookmarks

## Configuration

- AWS Glue Job: retailflow-etl
- Job Bookmarks: Enabled

## Purpose

Job Bookmarks are configured to support incremental processing by tracking previously processed input files. This allows the ETL job to skip already processed data on subsequent runs.

> Note: Incremental processing demonstration was not performed because the raw dataset had already been fully loaded before enabling Job Bookmarks.