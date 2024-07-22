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
curl -X POST http://localhost:4566/restapis/fxoa9zhl20/local/_user_request_/test   -H "Content-Type: application/json"   -d '{"real_number": "+16505604560"}' | jq
```

---

For hot reloading to work (very important!), you need to set `mountCode: true`:
```yml
custom:
  localstack:
    stages:
      - local
    lambda:
      mountCode: true # <<<
```