# Build stage
FROM python:3.9-alpine AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# Final stage
FROM python:3.9-alpine

WORKDIR /app

# Copy from builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app/server.py .

# Run Python directly
CMD ["python", "/app/server.py"]
