FROM python:3-slim

WORKDIR /code/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install lxml
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
COPY . .
EXPOSE 8080
EXPOSE 8000
EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT Summary.wsgi:application