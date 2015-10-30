FROM logstash:2.0.0
MAINTAINER Bahaaldine Azarmi <baha@elastic.co>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y supervisor curl

ADD etc/supervisor/conf.d/logstash.conf /etc/supervisor/conf.d/logstash.conf

EXPOSE 5043

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]

