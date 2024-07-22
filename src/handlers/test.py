# For hot-reload
# awslocal lambda create-function --function-name create_burner_number --code S3Bucket="hot-reload",S3Key="${PWD}" --handler src/handlers/create_burner_number.handler --runtime python3.10 --role arn:aws:iam::000000000000:role/lambda-ex


import sys
import os

# import subprocess
import glob

sys.path.insert(0, glob.glob(".venv/lib/python*/site-packages")[0])

import plivo


def handler(event, context):
    try:
        return {
            "statusCode": 200,
            "body": {
                "python_version": sys.version,
                "current_directory": os.getcwd(),
                "directory_contents": os.listdir(),
                "python_path": os.environ.get("PYTHONPATH"),
                "is_plivo_installed": "plivo" in sys.modules,
                "plivo_version": plivo.version.__version__,
            },
        }
    except ImportError as e:
        return {"statusCode": 500, "error": str(e)}
