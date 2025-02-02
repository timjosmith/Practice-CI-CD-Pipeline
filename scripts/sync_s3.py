import boto3
import os

def sync_file(source_bucket, destination_bucket, file_key):
    """
    Copy a specific file from the source S3 bucket to the destination S3 bucket.
    """
    s3 = boto3.client('s3')
    try:
        copy_source = {'Bucket': source_bucket, 'Key': file_key}
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=file_key)
        print(f"Successfully synced {file_key} from {source_bucket} to {destination_bucket}")
    except Exception as e:
        print(f"Error syncing file: {e}")
        raise

if __name__ == "__main__":
    source_bucket = os.getenv("SOURCE_BUCKET", "resume.staging.com")
    destination_bucket = os.getenv("DESTINATION_BUCKET", "testbucket07732")
    file_key = os.getenv("FILE_KEY", "index.html")

    if not source_bucket or not destination_bucket:
        raise ValueError("SOURCE_BUCKET and DESTINATION_BUCKET must be set")

    sync_file(source_bucket, destination_bucket, file_key)
