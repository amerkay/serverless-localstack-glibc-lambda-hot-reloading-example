import os

import sys
import glob

# for hot-reload on localstack
sys.path.insert(0, glob.glob(".venv/lib/python*/site-packages")[0])

import plivo


#####
# Test the endpoint (DON'T FORGET to replace /restapis/xxxx with your API Gateway ID)
#
# curl -X POST http://localhost:4566/restapis/20rox9lnk7/local/_user_request_/test -H "Content-Type: application/json" -d '{"real_number": "16505604560"}' | jq
#
#
# OR using ngrok:
# curl -X POST https://earwig-champion-broadly.ngrok-free.app/restapis/20rox9lnk7/local/_user_request_/test -H "Content-Type: application/json" -d '{"real_number": "16505604560"}' | jq
#####
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
