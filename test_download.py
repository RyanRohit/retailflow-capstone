from pathlib import Path

from s3_ingest.s3_manager import S3Manager
from s3_ingest.config import S3_BUCKET_NAME

s3 = S3Manager()

download_dir = Path("data/output")
download_dir.mkdir(parents=True, exist_ok=True)

download_path = download_dir / "customers_downloaded.csv"

s3.download_file(
    bucket=S3_BUCKET_NAME,
    object_name="raw/customers/customers.csv",
    download_path=str(download_path)
)

print("Download completed!")
print(f"Saved to: {download_path}")