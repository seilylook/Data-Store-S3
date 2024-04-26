import os
import boto3
import time

bucket = "2024-big-data-course-seilylook"
folder_name = "2024/"
path = "test.jpg"
obj = "test.jpg"

session = boto3.Session(profile_name="default")
s3 = session.client('s3')

print(folder_name + os.path.basename(path))

s3.download_file(bucket, folder_name+os.path.basename(path), "./"+os.path.basename(path)) 
