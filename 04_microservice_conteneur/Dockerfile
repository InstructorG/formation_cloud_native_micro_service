FROM python:3.10-slim

RUN mkdir -p /api

WORKDIR /api

RUN pip install -U pip

COPY requirements.txt  /api/

RUN pip install -r /api/requirements.txt

COPY database /api/database
COPY web /api/web
COPY core /api/core
COPY oas.yaml /api

EXPOSE 8000

CMD ["uvicorn", "web.main:app", "--host", "0.0.0.0"]