# python-cli-csv-to-multi-node-elasticsearch-client-without-ssl-sqlalchemy-simple

## Description
Reads a csv file into a multi node cluster for data in `dog-demo` document.

Uses sqlalchemy to connect and model data.

## Tech stack
- python
    - flask
    - sqlalchemy
    - elasticsearch
    - elasticsearch_dbapi
- elasticsearch
- kibana

## Docker stack
- python
- elasticsearch
- kibana

## To run
`sudo ./install.sh -u`

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Docker setup](https://lynn-kwong.medium.com/all-you-need-to-know-about-using-elasticsearch-in-python-b9ed00e0fdf0)
- [Search setup](https://www.elastic.co/guide/en/elasticsearch/client/python-api/master/examples.html)