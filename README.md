
## Setting up LocalStack dev mode with hot-reloading

1. Docker must be installed and running on your machine.

2. Run docker compose:
```sh
# clone the repo then cd into it
cd ~/devel/sn-number-masking
docker compose up
```

3. Create a virtual environment in the project root directory:
```sh
# this must match the in serverless.yml
python3.11 -m venv .venv

# activate the virtual environment we just created
source .venv/bin/activate

# Install the required packages with manylinux2014_x86_64 platform to avoid GLIBC errors
pip install -r requirements.txt --platform manylinux2014_x86_64 --only-binary=:all: --target .venv/lib/python3.11/site-packages
```

4. Install the serverless framework and dependencies:
```sh
pnpm install -g serverless
pnpm install
```

5. Deploy the stack:
```sh
serverless deploy --stage local
```

6. Test the endpoint
```sh
curl -X POST http://localhost:4566/restapis/apiid123/local/_user_request_/test   -H "Content-Type: application/json"   -d '{"real_number": "+16505604560"}' | jq
```

> Notice, we setup a static ID so the URLs don't keep changing: `apiid123`.

---

### Making sure the .venv is in the PYTHONPATH

If you get errors like `No module named 'plivo'`, this is the fix.

Your `./src/__init__.py` should look like this:
```python
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
```

### Your serverless.yml - enable mountCode to enable hot-reloading

For hot reloading to work (very important!), you need to set `mountCode: true`. See [Hot Reloading | LocalStack Docs](https://docs.localstack.cloud/user-guide/lambda-tools/hot-reloading/#hot-reloading-for-python-lambdas).

```yml
custom:
  localstack:
    stages:
      - local
    lambda:
      mountCode: true # <<<
```

---


## References
- [Hot Reloading | LocalStack Docs](https://docs.localstack.cloud/user-guide/lambda-tools/hot-reloading/#hot-reloading-for-python-lambdas)
- [LocalStack Serverless Plugin](https://www.serverless.com/plugins/serverless-localstack)
- [Serverless Python Requirements plugin docs](https://www.serverless.com/plugins/serverless-python-requirements)
- Discussion on GitHub: [Unable to import module 'api': /lib64/libc.so.6: version \`GLIBC\_2.28' not found - Issue #765 · serverless/serverless-python-requirements · GitHub](https://github.com/serverless/serverless-python-requirements/issues/765#issuecomment-1507138749) 