FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY run.sh .

RUN chmod a+x run.sh

CMD [ "./run.sh" ]
