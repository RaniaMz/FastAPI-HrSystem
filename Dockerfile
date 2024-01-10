FROM docker.io/tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
