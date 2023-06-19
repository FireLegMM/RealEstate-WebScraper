FROM python:3.10

RUN apt-get update && apt-get -y install cron vim
COPY ./crontab crontab
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN crontab crontab

WORKDIR /web-scraper


ENTRYPOINT ["tail", "-f", "/dev/null"]