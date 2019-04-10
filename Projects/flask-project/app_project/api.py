#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, url_for
import pymysql
from db import connection

app = Flask(__name__)

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


# Trang chủ
@app.route('/home')
def my_home():
    cursor = connection().cursor()
    query = "SELECT ten_mon, image from mon_an order by ma_mon limit 10"
    cursor.execute(query)
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
    return render_template('trangchu.html', getLink=getlinkstatic(), listmonan=listData)

# giao diện các công thức đơn vị
@app.route('/home/<donviCT>')
def itemCT(donviCT):
    
    return render_template('itemcongthuc.html', getLink=getlinkstatic(), title=donviCT)

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
    return render_template('meovaobep.html', getLink=getlinkstatic(), listmeovat = listData)

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
    return render_template('app_nauan.html', getLink=getlinkstatic(), title=title,mon=mon)

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
    return render_template('app_meovat.html', getLink=getlinkstatic(), meo=meo, title = tenmeovat)