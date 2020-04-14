#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from models import Mon_an, Meovaobep, Meovat
import os, base64, re
import certifi

# es = Elasticsearch('https://bd3gzan5ur:8i2skk418m@foodforfamily-821201285.ap-southeast-2.bonsaisearch.net:443')
# Parse the auth and host from env:
# bonsai = "https://bd3gzan5ur:8i2skk418m@foodforfamily-821201285.ap-southeast-2.bonsaisearch.net"
# auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
# host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

# print(auth)
# print(host)

# # Connect to cluster over SSL using auth for best security:
# es_header = [{
#  'host': host,
#  'port': 443,
#  'use_ssl': True,
#  'verify_certs': True,
#  'http_auth': (auth[0],auth[1]),
#  'ca_certs':certifi.where()
# }]

# Instantiate the new Elasticsearch connection:
es = Elasticsearch(es_header)

mon_an = Mon_an
meovaobep = Meovaobep
meovat = Meovat

def create_mon():
    table_name = mon_an.__table__.name
    results = mon_an.query.with_entities(mon_an.ma_mon, mon_an.ten_mon, mon_an.image, mon_an.cong_thuc, mon_an.nguyen_lieu, mon_an.video).all()
    for result in results:
        body = {
            "ten_mon": result[1],
            "image": result[2],
            "cong_thuc": result[3],
            "nguyen_lieu": result[4],
            "video": result[5]
        }
        es.index(index=table_name, doc_type=table_name, id = result[0], body = body)

def create_meovat():
    table_name = meovat.__table__.name
    results = meovat.query.with_entities(meovat.id, meovat.name, meovat.mo_ta).all()
    for result in results:
        body = {
            "name": result[1],
            "mo_ta": result[2]
        }
        es.index(index=table_name, doc_type=table_name, id = result[0], body = body)

def create_meovaobep():
    table_name = meovaobep.__table__.name
    results = meovaobep.query.with_entities(meovaobep.id, meovaobep.name, meovaobep.mo_ta, meovaobep.image).all()
    for result in results:
        body = {
            "name": result[1],
            "mo_ta": result[2],
            "image": result[3]
        }
        es.index(index=table_name, doc_type=table_name, id = result[0], body = body)
def create_all():
    create_mon()
    create_meovat()
    create_meovaobep()

def search_mon(query):
    body = {
        "_source": ["ten_mon", "image"],
        "query": {

            "multi_match" : {
            "query": query,
            "fields": [ "ten_mon"]
            }
        }
    }

    search = es.search(index = "mon_an", doc_type="mon_an", body = body)
    data = search['hits']['hits']
    return data

def search_meo(query, model):
    body = {
        "query": {
            "multi_match" : {
            "query": query,
            "fields": [ "name", "mo_ta"]
            }
        }
    }
    table_name = model.__table__.name
    search = es.search(index = table_name, doc_type=table_name, body = body)
    data = search['hits']['hits']
    return data


if __name__ == "__main__":
    # create_all()
    data = search_meo("các mẹo nhà bếp với tỏi", meovaobep)
    # data = search_mon("công thức làm món thịt chiên xù")
    for item in data:
        print(item['_source'])