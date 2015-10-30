FROM java:8
MAINTAINER Bahaaldine Azarmi <baha@elastic.co>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y supervisor curl git golang

RUN \
    git clone git://github.com/elasticsearch/logstash-forwarder.git && \
    mv logstash-forwarder /opt/logstash-forwarder && \
    cd /opt/logstash-forwarder && \
    go build -o logstash-forwarder

ADD etc/supervisor/conf.d/logstash-forwarder.conf /etc/supervisor/conf.d/logstash-forwarder.conf

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]

