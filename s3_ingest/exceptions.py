class S3UploadError(Exception):
    """Raised when an S3 upload fails."""
    pass


class S3DownloadError(Exception):
    """Raised when an S3 download fails."""
    pass