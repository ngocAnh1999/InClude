
from flask_sqlalchemy import SQLAlchemy
from __main__ import sqldb
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Mon_an(sqldb.Model):
    __tablename__ = 'mon_an'

    ma_mon = sqldb.Column(sqldb.Integer, primary_key = True)
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
        return "mon_an('{self.ten_mon}', '{self.image}', '{self.cong_thuc}', '{self.nguyen_lieu}', '{self.video}')"

class Thanh_phan(sqldb.Model):
    __tablename__ = 'thanh_phan'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    tphan = relationship("mon_an", backref="ma_nl")
    def __repr__(self):
        return "thanh_phan('{self.id}', '{self.name}')"

class Van_hoa(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    vhoa = relationship("mon_an", backref="ma_vh")
    def __repr__(self):
        return "van_hoa('{self.id}', '{self.name}')"


class Mua(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    mua = relationship("mon_an", backref="ma_mua")
    def __repr__(self):
        return "_mua('{self.id}', '{self.name}')"

class Cach_cb(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    cb = relationship("mon_an", backref="ma_cach_cb")
    def __repr__(self):
        return "cach_cb('{self.id}', '{self.name}')"
