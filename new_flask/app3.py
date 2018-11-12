#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql.cursors
from flask_api import FlaskAPI
from flask import request as flask_request
app = FlaskAPI(__name__)
import requests
import json

def getConnection():
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='ngocanh1999',                             
                                db='sinhvien',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful!!")
    return connection

@app.route('/users/')
def getUsers():
    

    response = {
        "status": {
            "message": "Predict All successful",
            "code": 200,
            "api_code": 0,
            "module": "",
            "err_code": 0
        },
        "history_id": 129911,
        "data": {
            "entities": [
                {
                    "end": 24,
                    "real_value": {
                        "result": "1995-08-24T12:00:00.000+07:00",
                        "year": "1995",
                        "day": "24",
                        "month": "8"
                    },
                    "value": "ngày 24 tháng 8 năm 1995",
                    "entity": "$datetime",
                    "start": 0
                }
            ],
            "intents": [
                {
                    "confidence": 0.99,
                    "label": "am_sang_duong"
                },
                {
                    "confidence": 0.01,
                    "label": "duong_sang_am"
                },
                {
                    "confidence": 0,
                    "label": "kiem_tra_ngay_hoang_dao"
                }
            ]
        }
    }

    try:
        with connection.cursor() as cursor:
        
    #         sql = "SELECT a.mssv, a.ho, b.hocphi FROM sinhvienk60 a, hocphik60 b where a.ho like b.ten"
    #         cursor.execute(sql)
            
    #         print ("cursor: ", cursor)

    #         print()

    #         users = []
    #         for row in cursor:
    #             user = {"ho": row['ho'], "hocphi": row['hocphi'], "mssv": row['mssv']}
    #             users.append(user)

    #             # return user  
            return json.dumps(response)
            
    finally:
        connection.close()

@app.route("/users/<name>/")
def getUserByName(name):
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
        
            sql = "SELECT a.mssv, a.ho, b.hocphi FROM sinhvienk60 a, hocphik60 b where a.ho like b.ten"
            cursor.execute(sql)
            
            print ("cursor: ", cursor)

            print()

            users = []
            for row in cursor:
                user = {"ho": row['ho'], "hocphi": row['hocphi'], "mssv": row['mssv']}
                if name == user['ho'] :
                    users.append(user)
            
                # return user  
            return users

            
    finally:
        connection.close()

@app.route("/predict", methods=["POST"])
def postRequest():
    
    thongTin = flask_request.data
    data = json.dumps(thongTin)

    #'select * from users where name = " + name + " and password = " + password 
   
    headers = {
        "Authorization": flask_request.headers["Authorization"]
    }

    url = "https://v3-api.fpt.ai/api/v3/predict"

    r = requests.post(url, data=data, headers=headers)
    
    return r.json()

    
if __name__ == '__main__':
    app.run()
