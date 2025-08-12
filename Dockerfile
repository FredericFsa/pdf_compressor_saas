FROM python:3.12-slim

# OS deps for PDF compression
RUN apt-get update && apt-get install -y --no-install-recommends \ 
    ghostscript qpdf poppler-utils \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Use gunicorn in prod; Render provides $PORT
ENV PORT=8000
EXPOSE 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "2"]
