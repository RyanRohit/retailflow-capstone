from pathlib import Path

from s3_ingest.s3_manager import S3Manager
from s3_ingest.config import S3_BUCKET_NAME


s3 = S3Manager()

DATA_DIR = Path("data/raw")

FILE_MAPPING = {
    "customers.csv": "raw/customers/customers.csv",
    "products.csv": "raw/products/products.csv",
    "orders_day1.json": "raw/orders/orders_day1.json",
    "orders_day2.json": "raw/orders/orders_day2.json",
    "order_items_day1.json": "raw/order_items/order_items_day1.json",
    "order_items_day2.json": "raw/order_items/order_items_day2.json",
    "clickstream_day1.json": "raw/clickstream/clickstream_day1.json",
    "clickstream_day2.json": "raw/clickstream/clickstream_day2.json",
}

for file_name, s3_key in FILE_MAPPING.items():

    file_path = DATA_DIR / file_name

    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    print(f"Uploading {file_name}...")

    s3.upload_file(
        str(file_path),
        S3_BUCKET_NAME,
        s3_key
    )

print("\nAll uploads completed successfully!")