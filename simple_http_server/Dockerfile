FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app/
COPY run.sh /app/

# Ensure correct permissions and line endings
RUN chmod +x /app/run.sh && \
    sed -i 's/\r$//' /app/run.sh

# Use sh to execute the script
CMD [ "sh", "-c", "/app/run.sh" ]
