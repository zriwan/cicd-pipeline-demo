from botocore.exceptions import ClientError, NoCredentialsError
from flask import Flask, render_template, request, redirect, url_for, send_file
import boto3
import os


app = Flask(__name__)

BUCKET_NAME = "zriwan-cicd-s3-demo-euw2"
s3 = boto3.client("s3")


@app.route("/")
def home():
    files = []
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if "Contents" in response:
            files = [obj["Key"] for obj in response["Contents"]]
    except (ClientError, NoCredentialsError) as e:
        print(e)

    return render_template("index.html", files=files)


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file.filename == "":
        return redirect(url_for("home"))

    s3.upload_fileobj(file, BUCKET_NAME, file.filename)

    return redirect(url_for("home"))


@app.route("/download/<filename>")
def download_file(filename):
    download_path = f"/tmp/{filename}"
    s3.download_file(BUCKET_NAME, filename, download_path)
    return send_file(download_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
