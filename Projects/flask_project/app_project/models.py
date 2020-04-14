#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from __main__ import sqldb
# from api import sqldb
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy as wa

class Mon_an(sqldb.Model):
    __tablename__ = 'mon_an'
    __searchable__ = ['ten_mon', 'cong_thuc', 'nguyen_lieu']
    ma_mon = sqldb.Column(sqldb.Integer, primary_key = True)
    ten_mon = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    image = sqldb.Column(sqldb.String(255), nullable = False)
    cong_thuc = sqldb.Column(sqldb.Text, nullable = False)
    nguyen_lieu = sqldb.Column(sqldb.Text, nullable = False)
    ma_nl = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('thanh_phan.id'), nullable = True)
    ma_vh = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('van_hoa.id'), nullable = True)
    ma_cach_cb = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('cach_cb.id'), nullable = True)
    ma_mua = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('_mua.id'), nullable = True)
    video = sqldb.Column(sqldb.String(255), nullable = True)

    def addMonan(self, ten_mon, image, cong_thuc, nguyen_lieu, ma_nl, ma_vh , ma_cach_cb, ma_mua , video):
        self.ten_mon = ten_mon
        self.image = image
        self.cong_thuc = cong_thuc
        self.nguyen_lieu = nguyen_lieu
        self.ma_nl = ma_nl
        self.ma_vh = ma_vh
        self.ma_cach_cb = ma_cach_cb
        self.ma_mua = ma_mua
        self.video = video
        sqldb.session.add(self)
        sqldb.session.commit()

    # def __repr__(self):
    #     return '%r' % self.ten_mon


class Thanh_phan(sqldb.Model):
    __tablename__ = 'thanh_phan'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)

# func add data to table thanh_phan
    def addThanhphan(self, excelValue):
        self.name = excelValue
        sqldb.session.add(self)
        sqldb.session.commit()

class Van_hoa(sqldb.Model):
    __tablename__ = 'van_hoa'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)

# func add data to table Van_hoa
    def addVanhoa(self, excelValue):
        self.name = excelValue
        sqldb.session.add(self)
        sqldb.session.commit()

class _mua(sqldb.Model):
    __tablename__ = '_mua'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)


# func add data to table _mua
    def addMua(self, excelValue):
        self.name = excelValue
        sqldb.session.add(self)
        sqldb.session.commit()

class Cach_cb(sqldb.Model):
    __tablename__ = 'cach_cb'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)

# func add data to table Cach_cb
    def addCachchebien(self, excelValue):
        self.name = excelValue
        sqldb.session.add(self)
        sqldb.session.commit()

class Meovaobep(sqldb.Model):
    __tablename__ = 'meovaobep'
    __searchable__ = ['name', 'mo_ta']
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    mo_ta = sqldb.Column(sqldb.Text, nullable = False)
    image = sqldb.Column(sqldb.String(255))
    id_meo = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('meovat.id'), nullable = True)

    def addMeovaobep(self, name, mo_ta, image, id_meo):
        self.name = name
        self.mo_ta = mo_ta
        self.image = image
        self.id_meo = id_meo
        sqldb.session.add(self)
        sqldb.session.commit()

class Meovat(sqldb.Model):
    __tablename__ = 'meovat'
    __searchable__ = ['name', 'mo_ta']
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    mo_ta = sqldb.Column(sqldb.Text, nullable = False)

    def addMeovat(self, name, mo_ta):
        self.name = name
        self.mo_ta = mo_ta
        sqldb.session.add(self)
        sqldb.session.commit()


if __name__ == "__main__":
    # sqldb.create_all()

    results = Mon_an.query.whoosh_search("cải thảo")
    print(results)


