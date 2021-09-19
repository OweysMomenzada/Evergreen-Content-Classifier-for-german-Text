FROM python:3.7

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip3 install -r requirements.txt
RUN pip install gunicorn


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
