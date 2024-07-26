import os
import sys
import glob


def is_running_on_localstack():
    """
    Determine if the current environment is running on LocalStack.
    """
    # Check for LocalStack-specific environment variable
    if os.environ.get("LOCALSTACK_HOSTNAME"):
        return True


# for hot-reload on
if is_running_on_localstack():
    """
    Add the .venv to localstack lambdas for hot-reload.
    See https://docs.localstack.cloud/user-guide/lambda-tools/hot-reloading/#hot-reloading-for-python-lambdas
    """
    sys.path.insert(0, glob.glob(".venv/lib/python*/site-packages")[0])
