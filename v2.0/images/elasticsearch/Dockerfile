FROM elasticsearch:2.0.0

MAINTAINER Bahaaldine Azarmi <baha@elastic.co>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y supervisor curl

ADD etc/supervisor/conf.d/elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

# Shield & Watcher & Marvel agent
RUN /usr/share/elasticsearch/bin/plugin install license
RUN /usr/share/elasticsearch/bin/plugin install watcher
RUN /usr/share/elasticsearch/bin/plugin install shield
RUN /usr/share/elasticsearch/bin/plugin install marvel-agent

EXPOSE 9200
EXPOSE 9300

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]
