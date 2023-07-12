FROM python:3.11.4

RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y --no-install-recommends mysql-client \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 \
    && sudo apt-get install python3-dev python3.11-dev default-libmysqlclient-dev build-essential \
    && pip install mysqlclient \
    && python install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /usr/src/app

COPY . .

CMD ["python3", "manage.py", "runserver"]

EXPOSE 3000