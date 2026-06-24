import boto3

bucket_name = "zriwan-cicd-s3-demo-euw2"
object_name = "test.txt"
download_path = "downloaded_test.txt"

s3 = boto3.client("s3")

s3.download_file(bucket_name, object_name, download_path)

print("File downloaded successfully!")
