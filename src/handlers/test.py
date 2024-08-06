import os
import sys
import plivo


#####
# Test the endpoint:
#
# curl -X POST http://localhost:4566/restapis/apiid123/local/_user_request_/test -H "Content-Type: application/json" -d '{"real_number": "16505604560"}' | jq
#
#
# OR using ngrok:
# curl -X POST https://earwig-champion-broadly.ngrok-free.app/restapis/apiid123/local/_user_request_/test -H "Content-Type: application/json" -d '{"real_number": "16505604560"}' | jq
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
