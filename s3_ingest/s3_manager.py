import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
from tenacity import retry, stop_after_attempt, wait_exponential

from .config import AWS_REGION
from .logger import logger
from .exceptions import S3UploadError, S3DownloadError


class S3Manager:
    def __init__(self):
        print("AWS_REGION =", AWS_REGION)
        print("Creating S3 client...")
        self.client = boto3.client(
        "s3",
        region_name=AWS_REGION,
        config=Config(signature_version="s3v4")
        )
        print("Endpoint:", self.client.meta.endpoint_url)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1)
    )
    def upload_file(self, file_path, bucket, object_name):

        try:

            self.client.upload_file(
                file_path,
                bucket,
                object_name
            )

            logger.info(
                f"Successfully uploaded '{object_name}'"
            )

        except ClientError as e:

            logger.error(e)

            raise S3UploadError(e)
        
    def list_objects(self, bucket):

        response = self.client.list_objects_v2(
            Bucket=bucket
        )

        if "Contents" not in response:
            return []

        return [
            obj["Key"]
            for obj in response["Contents"]
        ]
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1)
    )
    def download_file(
        self,
        bucket,
        object_name,
        download_path
    ):

        try:

            self.client.download_file(
                bucket,
                object_name,
                download_path
            )

            logger.info(
                f"Downloaded '{object_name}'"
            )

        except ClientError as e:

            logger.error(e)

            raise S3DownloadError(e)
    
    def delete_object(
        self,
        bucket,
        object_name
    ):

        self.client.delete_object(
            Bucket=bucket,
            Key=object_name
        )

        logger.info(
            f"Deleted '{object_name}'"
        )

    def generate_presigned_url(
        self,
        bucket,
        object_name,
        expiration=3600
    ):

        return self.client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": bucket,
                "Key": object_name
            },
            ExpiresIn=expiration
        )