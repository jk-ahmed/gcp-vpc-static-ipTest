FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Copy and install only the requirements first (to leverage caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application code
COPY . .

# Expose port and define the container entrypoint.
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "300", "--access-logfile", "-", "--error-logfile", "-", "main:app"]
