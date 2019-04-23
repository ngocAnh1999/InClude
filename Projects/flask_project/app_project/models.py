#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
# from __main__ import sqldb
from api import sqldb
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Mon_an(sqldb.Model):
    __tablename__ = 'mon_an'

    ma_mon = sqldb.Column(sqldb.Integer, primary_key = True, auto_increment = True)
    ten_mon = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    image = sqldb.Column(sqldb.String(255), nullable = False)
    cong_thuc = sqldb.Column(sqldb.Text, nullable = False)
    nguyen_lieu = sqldb.Column(sqldb.Text, nullable = False)
    ma_nl = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('thanh_phan.id'), nullable = True)
    ma_vh = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('van_hoa.id'), nullable = True)
    ma_cach_cb = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('cach_cb.id'), nullable = True)
    ma_mua = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('_mua.id'), nullable = True)
    video = sqldb.Column(sqldb.String(255), nullable = False)
    def __repr__(self):
        return '<Mon_an %r>' % self.ten_mon

class Thanh_phan(sqldb.Model):
    __tablename__ = 'thanh_phan'
    id = sqldb.Column(sqldb.Integer, primary_key = True, auto_increment = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    # ma_nl = relationship("Mon_an", backref="ma_nl")
    def _ma_nl_repr__(self):
        return '<Thanh_phan %r>' % self.name

    def __init__(self, excelValue):
        self.name = excelValue



class Van_hoa(sqldb.Model):
    __tablename__ = 'van_hoa'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    # ma_vh = relationship("Mon_an", backref="ma_vh")
    def __repr__(self):
        return '<Van_hoa %r>' % self.name


class _mua(sqldb.Model):
    __tablename__ = '_mua'
    id = sqldb.Column(sqldb.Integer, primary_key = True, auto_increment = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    # ma_mua = relationship("Mon_an", backref="ma_mua")
    def __repr__(self):
        return '<_mua %r>' % self.name
    def __init__(self, excelValue):
        # self.id = excelId
        self.name = excelValue

class Cach_cb(sqldb.Model):
    __tablename__ = 'cach_cb'
    id = sqldb.Column(sqldb.Integer, primary_key = True, auto_increment = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    # ma_cach_cb = relationship("Mon_an", backref="ma_cach_cb")
    def __repr__(self):
        return '<Cach_cb %r>' % self.name


if __name__ == '__main__':
    # xuan = Mua(name = "Mùa xuân")
    # sqldb.session.add(xuan)
    # sqldb.session.commit()
    # results = _mua.
    # print(results[1])
    sqldb.create_all()

