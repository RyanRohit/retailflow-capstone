from s3_ingest.s3_manager import S3Manager
from s3_ingest.config import S3_BUCKET_NAME

s3 = S3Manager()

print("Connected successfully!")

print(s3.list_objects(S3_BUCKET_NAME))