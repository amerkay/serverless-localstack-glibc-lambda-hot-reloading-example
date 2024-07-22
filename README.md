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
python3.10 -m venv .venv

# activate the virtual environment we just created
source .venv/bin/activate
```

4. Install the required packages with manylinux2014_x86_64 platform to avoid GLIBC errors:
```sh
pip install -r requirements.txt --platform manylinux2014_x86_64 --only-binary=:all: --target .venv/lib/python3.11/site-packages
```

5. Install the serverless framework:
```sh
pnpm install -g serverless
pnpm install
```

6. Deploy the stack:
```sh
serverless deploy --stage local
```

7. Test the endpoint
```sh
curl -X POST http://localhost:4566/restapis/hpdhundh6z/local/_user_request_/test   -H "Content-Type: application/json"   -d '{"real_number": "+16505604560"}' | jq
```

---


## References
- [Hot Reloading | LocalStack Docs](https://docs.localstack.cloud/user-guide/lambda-tools/hot-reloading/#hot-reloading-for-python-lambdas)
- [LocalStack Serverless Plugin](https://www.serverless.com/plugins/serverless-localstack)
- [Serverless Python Requirements plugin docs](https://www.serverless.com/plugins/serverless-python-requirements)
- Discussion on GitHub: [Unable to import module 'api': /lib64/libc.so.6: version \`GLIBC\_2.28' not found - Issue #765 · serverless/serverless-python-requirements · GitHub](https://github.com/serverless/serverless-python-requirements/issues/765#issuecomment-1507138749) 


## Notes:
For hot reloading to work (very important!), you need to set `mountCode: true`. See [Hot Reloading | LocalStack Docs](https://docs.localstack.cloud/user-guide/lambda-tools/hot-reloading/#hot-reloading-for-python-lambdas).

```yml
custom:
  localstack:
    stages:
      - local
    lambda:
      mountCode: true # <<<
```

## TODOs:
- [ ] Make sure online deployment works correctly.
