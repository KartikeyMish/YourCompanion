# Test Run (locally) 
`poetry run python cli.py test main.py`

# POST req. response

POST `http://localhost:8080/chat`

```
body:
{
  "messages": [
    {"text": "Hi, I want to know if its possible to read 10 books at once.", "sender": "user"},
    {"text": "I wanted to know if there's a way to book cheaper flights", "sender": "user"},
    {"text": "What's the weather like today?", "sender": "user"}
  ]
}
```

![demo](textbase/frontend/public/demo.png)

# Building cli locally
inside pyproject.toml add (if not included yet)-
```toml
[tool.poetry.scripts]
textbase = "textbase.textbase_cli:cli"
```

```bash
poetry build
pip install dist/textbase-0.1.0.tar.gz
```

```bash
textbase test main.py
```

# Local web hosting using `textbase test main.py`
![chat](textbase/frontend/public/chat.png)

## Docker
Local setup
docker build -t my_fastapi_app .
docker build --platform=linux/amd64 -t my_fastapi_app .
docker run -p 8080:8080 my_fastapi_app

For GCP
docker build -t gcr.io/[YOUR_PROJECT_ID]/my_fastapi_app .
docker build --platform=linux/amd64 -t gcr.io/[YOUR_PROJECT_ID]/my_fastapi_app .
docker push gcr.io/[YOUR_PROJECT_ID]/my_fastapi_app

gcloud run deploy --image gcr.io/[YOUR_PROJECT_ID]/my_fastapi_app --platform managed --port 8080 --allow-unauthenticated

https://textbase-app-soe52x2r4a-uc.a.run.app
