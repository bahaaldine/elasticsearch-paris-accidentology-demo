FROM elasticsearch:1.6.2

MAINTAINER Bahaaldine Azarmi <baha@elastic.co>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y supervisor curl

ADD etc/supervisor/conf.d/elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

# Marvel
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/marvel/1.3.1
# Shield 
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/license/1.0.0
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/shield/1.3.1
# Watcher
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/watcher/1.0.1 -Des.path.conf=/etc/elasticsearch

EXPOSE 9200
EXPOSE 9300

CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf" ]