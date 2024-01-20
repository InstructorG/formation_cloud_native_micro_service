FROM python:3.10-slim

RUN mkdir -p /api

WORKDIR /api

RUN pip install -U pip

COPY requirements.txt  /api/

RUN pip install -r /api/requirements.txt

COPY src/microservice /api/microservice

EXPOSE 8003

CMD ["uvicorn", "microservice.payment.api:app", "--host", "0.0.0.0","--port","8003"]