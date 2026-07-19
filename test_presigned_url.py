from s3_ingest.s3_manager import S3Manager
from s3_ingest.config import S3_BUCKET_NAME

s3 = S3Manager()

url = s3.generate_presigned_url(
    bucket=S3_BUCKET_NAME,
    object_name="raw/customers/customers.csv"
)

print(url)