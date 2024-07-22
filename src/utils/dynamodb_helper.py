import boto3
import os


def get_dynamodb_table(table_name):
    if os.environ.get("IS_OFFLINE"):
        dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566")
    else:
        dynamodb = boto3.resource("dynamodb")
    return dynamodb.Table(table_name)
