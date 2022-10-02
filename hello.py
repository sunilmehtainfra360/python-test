import os # For environmental variables when running in CodeBuild, Fargate, Lambda, etc.
import boto3 # Because you need it lol
import botocore # For Error Handling
import json # To parse "stringified" JSON Policy documents
import time # to create Unix timestamps for DynamoDB TTL
import multiprocessing
import hashlib # To create unique IDs for places where AWS doesn't have them
from botocore.config import Config

for bucket in s3_resource.buckets.all():
        print(bucket.name)
