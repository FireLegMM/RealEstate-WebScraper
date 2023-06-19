FROM python:3.10

RUN apt-get update && apt-get -y install cron vim
COPY ./crontab.cron crontab.cron
COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN crontab crontab.cron
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log