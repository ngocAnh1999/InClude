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

from models import Mon_an, Thanh_phan, Van_hoa, Cach_cb, _mua, Meovaobep, Meovat

def getlinkstatic():

    getLink=[{
        "linkTrangchu": url_for('my_home'),
        "linkMua": url_for('itemCT', donviCT="_mua", category = 'all'),
        "linkCachchebien": url_for('itemCT', donviCT="cach_cb", category = 'all'),
        "linkThanhphan": url_for('itemCT', donviCT="thanh_phan", category = 'all'),
        "linkVanhoa": url_for('itemCT', donviCT="van_hoa", category = 'all'),
        "linkMeovaobep": url_for('meovat')
    }]
    
    return getLink

def getListDishes(results):
    listData = []
    for result in results:
        jsonData = {
            "tenmon": result[0],
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

def model(donviCT):
    switcher = {
        "_mua": _mua,
        "cach_cb": Cach_cb,
        "thanh_phan": Thanh_phan,
        "van_hoa": Van_hoa,
    }
    return switcher.get(donviCT)

def query(donviCT, category):
    if category == 'all':

        switcher = {
            "_mua": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(_mua).filter(Mon_an.ma_mua == _mua.id).all(),
            "cach_cb": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(Cach_cb).filter(Mon_an.ma_cach_cb == Cach_cb.id).all(),
            "thanh_phan": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(Thanh_phan).filter(Mon_an.ma_nl == Thanh_phan.id).all(),
            "van_hoa": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(Van_hoa).filter(Mon_an.ma_vh == Van_hoa.id).all(),
        }
        return switcher.get(donviCT)
    else:
        switcher = {
            "_mua": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(_mua).filter(Mon_an.ma_mua == _mua.id).filter(_mua.name == category).all(),
            "cach_cb": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(Cach_cb).filter(Mon_an.ma_cach_cb == Cach_cb.id).filter(Cach_cb.name == category).all(),
            "thanh_phan": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(Thanh_phan).filter(Mon_an.ma_nl == Thanh_phan.id).filter(Thanh_phan.name == category).all(),
            "van_hoa": Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
            join(Van_hoa).filter(Mon_an.ma_vh == Van_hoa.id).filter(Van_hoa.name == category).all(),
        }
        return switcher.get(donviCT)
# Trang chủ
@app.route('/home')
def my_home():
    results = Mon_an.query.with_entities(Mon_an.ten_mon, Mon_an.image).\
        order_by(Mon_an.ma_mon.desc()).limit(10).all()
    listData = getListDishes(results)
    return render_template('trangchu.html', getLink=getlinkstatic(), listmonan=listData, menu=getlinkstatic())

# giao diện các công thức đơn vị
@app.route('/home/<donviCT>')
def itemCT(donviCT):
    category = request.args.get('category')
    class_name = model(donviCT)
    results = class_name.query.with_entities(class_name.name).all()
    congthucnauan = []
    for result in results:
        jsonData = {
            "link": url_for('itemCT', donviCT = donviCT, category = result[0]),
            "name": result[0]
        }
        congthucnauan.append(jsonData)

    res = query(donviCT, category)
    listmonan = []
    for re in res:
        jsonData = {
            "linkMon": url_for('monan', tenmon = re[0]),
            "linkImg": re[1],
            "tenmon": re[0]
        }
        listmonan.append(jsonData)

    return render_template('itemcongthuc.html', getLink=getlinkstatic(), title = getTitle(donviCT), congthucnauan = congthucnauan, listmonan = listmonan)

@app.route('/home/meovaobep')
def meovat():
    results = Meovat.query.with_entities(Meovat.name, Meovat.mo_ta).order_by(Meovat.id.desc()).limit(10).all()
    listData = []
    for result in results:
        jsonData = {
            "Ten": result[0],
            "mota": result[1], 
            "linkMeovat": url_for('meovaobep', tenmeovat= result[0])
        }
        listData.append(jsonData)
    connection().close()
    return render_template('meovaobep.html', getLink=getlinkstatic(), listmeovat = listData, menu=getlinkstatic())

# giao diện công thức món ăn cụ thể
@app.route('/home/congthucnauan/<tenmon>')
def monan(tenmon):
    results = Mon_an.query.\
        with_entities(Mon_an.ten_mon, Mon_an.cong_thuc, Mon_an.nguyen_lieu, Mon_an.image, Mon_an.video).\
        filter(Mon_an.ten_mon == tenmon).order_by(Mon_an.ma_mon.desc()).all()
    mon = []
    for result in results:
        jsonData = {"ten_mon": result[0], 
                    "cong_thuc": result[1], 
                    "nguyen_lieu": result[2], 
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
    results = Meovaobep.query.\
        with_entities(Meovaobep.name, Meovaobep.mo_ta, Meovaobep.image).\
            join(Meovat).filter(Meovaobep.id_meo == Meovat.id).filter(Meovat.name == tenmeovat).all()
    meo = []
    for result in results:
        jsonData = {
            "name": resullt[0],
            "mota": result[1],
            "image": result[2]
        }
        meo.append(jsonData)
    connection().close()
    return render_template('app_meovat.html', getLink=getlinkstatic(), meo=meo, title = tenmeovat, menu=getlinkstatic())


if __name__ == '__main__':
    app.run(debug= True)
