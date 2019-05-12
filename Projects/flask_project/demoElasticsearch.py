#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
from app_project import mon_an, meovaobep, meovat

es = Elasticsearch('http://localhost:9200')

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

if __name__ == "__main__":
    # create_all()
    body = {
        "_source": ["ten_mon"],
        "query": {
            "multi_match" : {
            "query": "cách làm món cơm chiên",
            "fields": [ "ten_mon", "cong_thuc" ]
            }
        }
    }

    search = es.search(index = "mon_an", doc_type = "mon_an", body = body)
    print(search['hits'])