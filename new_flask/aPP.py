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
                                db='user',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful!!")
    return connection

@app.route("/testUser", methods=["POST"])
def requestData():
    connection = getConnection()

    data = flask_request.data
    #data = json.dumps(thongTin)
    username = data['username']
    password = data['password']
    
  
    with connection.cursor() as cursors:
        sql = "select * from users where name = %s and password = %s"
        # sql = "select * from users where name = 'Anh' and password = 'anh199'"
        cursors.execute(sql, (username, password))
        arr = []
        for row in cursors:
            arr.append(row)
        if len(arr) == 0:
            return "không tồn tại username"
        return "có tồn tại người dùng này"
    

if __name__ == '__main__':
    app.run()
