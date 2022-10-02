import os # For environmental variables when running in CodeBuild, Fargate, Lambda, etc.
import boto3 # Because you need it lol
import botocore # For Error Handling
import json # To parse "stringified" JSON Policy documents
import time # to create Unix timestamps for DynamoDB TTL
import multiprocessing
import hashlib # To create unique IDs for places where AWS doesn't have them
from botocore.config import Config
from botocore.exceptions import ClientError


s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
for bucket in response:
    print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))
