#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, url_for
import pymysql
from flask_sqlalchemy import SQLAlchemy
from db import connection, host, user, password, dbname


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(user, password, dbname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sqldb = SQLAlchemy(app)

# from models import mon_an

def getlinkstatic():

    getLink=[{
        "linkTrangchu": url_for('my_home'),
        "linkMua": url_for('itemCT', donviCT="_mua"),
        "linkCachchebien": url_for('itemCT', donviCT="cach_cb"),
        "linkThanhphan": url_for('itemCT', donviCT="thanh_phan"),
        "linkVanhoa": url_for('itemCT', donviCT="van_hoa"),
        "linkMeovaobep": url_for('meovat')
    }]
    
    return getLink

def getListDishes(sql):
    cursor = connection().cursor()
    
    cursor.execute(sql)
    results = cursor.fetchall()
    listData = []
    for result in results:
        jsonData = {
            "tenmon": result[0].decode('utf-8'),
            "linkImg": result[1], 
            "linkMon": url_for('monan', tenmon=result[0])
        }
        listData.append(jsonData)
    connection().close()
    return listData

def getTitle(donviCT):
    switcher = {
        "_mua": "Món ăn theo mùa".decode('utf-8'),
        "cach_cb": "Món ăn theo cách chế biến".decode('utf-8'),
        "thanh_phan": "Món ăn theo thành phần".decode('utf-8'),
        "van_hoa": "Món ăn theo văn hóa".decode('utf-8'),
    }
    return switcher.get(donviCT, "Trang chủ".decode('utf-8'))

# Trang chủ
@app.route('/home')
def my_home():
    query = "SELECT ten_mon, image from mon_an order by ma_mon limit 10"
    listData = getListDishes(query)
    return render_template('trangchu.html', getLink=getlinkstatic(), listmonan=listData, menu=getlinkstatic())

# giao diện các công thức đơn vị
@app.route('/home/<donviCT>')
def itemCT(donviCT):
    
    return render_template('itemcongthuc.html', getLink=getlinkstatic(), title=getTitle(donviCT), menu=getlinkstatic())

# giao diện mẹo vào bếp
@app.route('/home/meovaobep')
def meovat():
    cursor = connection().cursor()
    query = "SELECT Ten, mota FROM meovat order by ID limit 10"
    cursor.execute(query)
    results = cursor.fetchall()
    listData = []
    for result in results:
        jsonData = {
            "Ten": result[0].decode('utf-8'),
            "mota": result[1].decode('utf-8'), 
            "linkMeovat": url_for('meovaobep', tenmeovat= result[0])
        }
        listData.append(jsonData)
    connection().close()
    return render_template('meovaobep.html', getLink=getlinkstatic(), listmeovat = listData, menu=getlinkstatic())

# giao diện công thức món ăn cụ thể
@app.route('/home/congthucnauan/<tenmon>')
def monan(tenmon):
    cursor = connection().cursor()
    # lay thong tin mon an
    sql2 = "SELECT ten_mon, cong_thuc, nguyen_lieu, image, video FROM mon_an where ten_mon like %s"
    cursor.execute(sql2,(tenmon,))
    results = cursor.fetchall()
    mon = []
    for result in results:
        jsonData = {"ten_mon": result[0].decode('utf-8'), 
                    "cong_thuc": result[1].decode('utf-8'), 
                    "nguyen_lieu": result[2].decode('utf-8'), 
                    "image": result[3],
                    "linkVideo": result[4]
                    }
        mon.append(jsonData)
    # print(mon)
    title= tenmon
    connection().close()
    return render_template('app_nauan.html', getLink=getlinkstatic(), title=title,mon=mon, menu=getlinkstatic())

# giao diện mẹo vặt cụ thể
@app.route('/home/meo_vao_bep/<tenmeovat>')
def meovaobep(tenmeovat):
    cursor = connection().cursor()
    query = "SELECT meobep.mota, meobep.img from meobep inner join meovat on meobep.ID=meovat.ID where meovat.Ten like %s"
    cursor.execute(query, (tenmeovat,))
    results = cursor.fetchall()
    meo = []
    for result in results:
        jsonData = {
            "image": result[1],
            "mota": result[0].decode('utf-8')
        }
        meo.append(jsonData)
    connection().close()
    return render_template('app_meovat.html', getLink=getlinkstatic(), meo=meo, title = tenmeovat, menu=getlinkstatic())


if __name__ == '__main__':
    app.run(debug= True)