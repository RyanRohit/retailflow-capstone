from s3_ingest.s3_manager import S3Manager
from s3_ingest.config import S3_BUCKET_NAME

s3 = S3Manager()

TEST_KEY = "logs/test_delete.txt"

# Upload a small test file first
with open("temp.txt", "w") as f:
    f.write("Delete me")

s3.upload_file(
    "temp.txt",
    S3_BUCKET_NAME,
    TEST_KEY
)

print("Uploaded test file.")

# Now delete it
s3.delete_object(
    S3_BUCKET_NAME,
    TEST_KEY
)

print("Deleted successfully.")