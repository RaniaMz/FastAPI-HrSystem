FROM docker.io/tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /web

COPY . /web

RUN pip3 --no-cache-dir  install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
