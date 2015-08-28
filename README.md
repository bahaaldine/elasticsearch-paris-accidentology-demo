# elasticsearch-paris-accidentology-demo

## Introduction ##

This Docker Compose project is an application which intends to demonstrate
ELK capabilities through Paris city accidentology use case

## Architecture

This application is a ES based logging architecture that combines: 
- A logtsash-forwarder that consumes the source/accidentology-with-geo-final.csv file
- A logstash instance that processes the message before pushing to a Kafka cluster
- A Kafka cluster (composed of 2 instances) that receives message and buffer them
- A logstash instance that indexes the message in Elasticsearch
- A single Elasticsearch node cluster
- A Kibana 4 instance to visualize the data

This application also showcases Elasticsearch commercial plugin:
- Marvel is installed and let you follow the activity of the ES cluster
- Shield is included and secure the overall ES cluster: you need 
to refer to the below [LDAP](https://github.com/bahaaldine/elasticsearch-paris-accidentology-demo/blob/master/README.md#ldap-users-and-groups) section to understand which user should be used in order
to interact with the cluster.
- Watcher is installed but no watch are included.

## Running the application ##

Use Docker Compose in the project root folder to launch the application: 

```bash
docker-compose up

```

## LDAP Users and Groups ##

This application is using the users and groups present by default in the LDAP.

### Groups ###

The DN template used to designate all groups is:

    `ou={GROUP_NAME},dc=elastic,dc=co`

There are 3 groups : Users, Marvels and Watcher

### Users ###

The DN template used to designate all users is:

    `cn={USER_NAME},ou={GROUP_NAME},dc=elastic,dc=co`

Here is the list of users splitted by groups:

- Users:
    - bahaaldine / bazarmi
    - morgan / mgoeller
    - steve / smayzak
    - dimitri / dmarx
    - matias / mcascallares

- Marvels
    - alan / ahardy
    - christoph / cwurm
    - david / derickson
    - agent / amarvel

- Watchers
    - antoine / agirbal
    - catherine / cjohnson
    - christian / cdahlqvist
    - jeremy / jhorton
    - peter / pkim

The LDAP admin user has the following credentials:

DN: cn=admin,dc=elastic,dc=co
user : admin
password:  password
