FROM python:3.11.5

RUN mkdir /fastapi

WORKDIR /fastapi

COPY deps.txt .

RUN pip install -r deps.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000