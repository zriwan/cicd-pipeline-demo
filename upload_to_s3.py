import boto3

bucket_name = "zriwan-cicd-s3-demo-euw2"
file_name = "test.txt"

s3 = boto3.client("s3")

s3.upload_file(file_name, bucket_name, file_name)

print("✅ File uploaded successfully!")
