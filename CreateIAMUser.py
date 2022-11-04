import json
import boto3

iam = boto3.client('iam')


def lambda_handler(event, context):
    response = iam.create_user(UserName='testmeuser')
    print(response)
