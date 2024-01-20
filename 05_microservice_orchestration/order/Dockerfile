FROM python:3.10-slim

RUN mkdir -p /api

WORKDIR /api

RUN pip install -U pip

COPY requirements.txt  /api/

RUN pip install -r /api/requirements.txt

COPY src/microservice /api/microservice

EXPOSE 8004

CMD ["uvicorn", "microservice.order.api:app", "--host", "0.0.0.0","--port","8004"]