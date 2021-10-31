# Define baseimage
FROM continuumio/miniconda3

ENV PATH /usr/local/bin/:$PATH

COPY . /app/

# Python Installation
RUN conda install -y python==3.8 \
    && conda clean -ya

# To install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "mlfastapi:app", "--host", "0.0.0.0", "--port", "8000"]