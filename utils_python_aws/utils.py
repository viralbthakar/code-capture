import re
import boto3
import logging

logger = logging.getLogger(__name__)


def extract_bucket_key_from_s3_uri(s3_uri):
    """
    Extracts the bucket name and key from an S3 URI.
    Args:
        s3_uri (str): The S3 URI in the format 's3://bucket_name/key'.
    Returns:
        tuple: A tuple containing the bucket name and key as strings.
    """
    s3_pattern = re.compile(r"^s3://([^/]+)/(.*)$")
    match = s3_pattern.match(s3_uri)
    bucket_name = match.group(1)
    key = match.group(2)
    return bucket_name, key


def upload_file_to_s3(file_path, s3_uri):
    """
    Uploads a file to an S3 bucket.
    Args:
        file_path (str): The local path of the file to upload.
        s3_uri (str): The S3 URI of the file to upload.
    Returns:
        bool: True if the file was uploaded successfully, False otherwise.
    """
    bucket_name, key = extract_bucket_key_from_s3_uri(s3_uri)
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket_name, key)
        return True
    except Exception as e:
        logger.error(f"Error uploading file to S3: {s3_uri}: {e}")
        return False


def download_file_from_s3(s3_uri, file_path):
    """
    Downloads a file from an S3 bucket.
    Args:
        s3_uri (str): The S3 URI of the file to download.
        file_path (str): The local path to save the downloaded file.
    Returns:
        bool: True if the file was downloaded successfully, False otherwise.
    """
    bucket_name, key = extract_bucket_key_from_s3_uri(s3_uri)
    s3 = boto3.client("s3")
    try:
        s3.download_file(bucket_name, key, file_path)
        return True
    except Exception as e:
        logger.error(f"Error downloading file from S3: {s3_uri}: {e}")
        return False
