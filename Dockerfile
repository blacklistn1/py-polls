FROM python:3.11.4-slim

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3-dev python3.11-dev default-libmysqlclient-dev build-essential pkg-config \
    && export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags` \
    && export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs` \
    && pip install mysqlclient

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python -m venv venv

RUN pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python3", "manage.py", "runserver"]
