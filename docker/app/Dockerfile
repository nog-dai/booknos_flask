FROM python:3.9.12-buster

ENV TZ="Asia/Tokyo" \
    LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

RUN apt update \
  && apt install -y gcc vim tree lsof

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT ["uwsgi", "--ini", "/var/www/app/uwsgi.ini"]
