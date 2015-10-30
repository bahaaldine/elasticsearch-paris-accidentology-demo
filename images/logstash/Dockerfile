FROM logstash:1.5.4-1
MAINTAINER Bahaaldine Azarmi <baha@elastic.co>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y supervisor curl

RUN /opt/logstash/bin/plugin install logstash-input-lumberjack
RUN /opt/logstash/bin/plugin install --version 1.0.5 logstash-input-lumberjack

ADD etc/supervisor/conf.d/logstash.conf /etc/supervisor/conf.d/logstash.conf

EXPOSE 5043

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]

