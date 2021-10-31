# Define baseimage
FROM python:3.8.12-slim

ENV PATH /usr/local/bin/:$PATH

WORKDIR /home/bayeslabs/app
COPY . /home/bayeslabs/app/

# To install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]