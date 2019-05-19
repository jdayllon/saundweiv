FROM jfloff/alpine-python:3.7-slim
#FROM frankierr/docker-apertium-all-dev
MAINTAINER Juan David Ayllón Burguillo <jdayllon@gmail.com>

USER root

# Install pipenv
RUN pip install --upgrade pip

# Install Leiserbik
WORKDIR /tmp
RUN wget -P /tmp https://github.com/jdayllon/leiserbik/archive/master.zip
RUN unzip master.zip
RUN rm -rf master.zip
WORKDIR /tmp/leiserbik-master
#RUN ls -al
RUN python setup.py install

# Install node
RUN apk add --update nodejs nodejs-npm wget curl supervisor

# Frontail
RUN npm install frontail -g

RUN mkdir /work
ENV WORK_DIR="/work/"
RUN touch /work/statuses
COPY run_tail.sh /root/run_tail.sh
COPY directory_checker.py /root/directory_checker.py
RUN chmod +x /root/run_tail.sh
RUN chmod +x /root/directory_checker.py

# Install Crontab Manager

RUN mkdir /crontab-ui; touch /etc/crontabs/root; chmod +x /etc/crontabs/root
WORKDIR /crontab-ui

COPY supervisord.conf /etc/supervisord.conf

RUN npm install -g crontab-ui

ENV   HOST 0.0.0.0
ENV   PORT 8000

ENV   CRON_PATH /etc/crontabs
#ENV   CRON_IN_DOCKER true

EXPOSE $PORT

CMD ["supervisord", "-c", "/etc/supervisord.conf"]

# CUSTOMIZATION CRONTAB-UI
COPY crontab.db /usr/lib/node_modules/crontab-ui/crontabs/crontab.db
RUN touch /usr/lib/node_modules/crontab-ui/crontabs/env.db
COPY crontab.script /etc/crontabs/root