import boto3

bucket_name = "zriwan-cicd-s3-demo-euw2"

s3 = boto3.client("s3")

response = s3.list_objects_v2(Bucket=bucket_name)

print("Files in bucket:")

if "Contents" in response:
    for obj in response["Contents"]:
        print(f"- {obj['Key']}")
else:
    print("Bucket is empty.")
