# Define baseimage
FROM python:3.8.12-slim-buster

COPY . /app/

WORKDIR /app

# To install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "mlfastapi:app", "--host", "0.0.0.0", "--port", "8000"]