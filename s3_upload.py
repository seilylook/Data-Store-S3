import os
import boto3
import time

bucket = "2024-big-data-course-seilylook"
obj = "test.jpg"
local_file_path = os.getcwd() + "/" + obj
target_file_name = "new_test_image.jpg"

session = boto3.Session(profile_name="default")
s3 = session.client('s3')

s3.upload_file(local_file_path, bucket, target_file_name)
