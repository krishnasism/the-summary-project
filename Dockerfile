FROM python:3-slim

WORKDIR /code/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install lxml
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
COPY . .