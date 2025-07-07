# static ip test

## Usage

This Flask app sends a periodic outbound HTTP request every 5 minutes.

## Build & Run Locally

```bash
docker build -t static-ip-test .
docker run -p 8080:8080 static-ip-test
```

## Deploy to Google Cloud Run

See `cloudbuild.yaml` for build and deployment steps.

## Requirements

- Python 3.12
- Flask
- Gunicorn
- pandas
- requests