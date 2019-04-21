
from flask_sqlalchemy import SQLAlchemy
from api import sqldb
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class mon_an(sqldb.Model):
    __tablename__ = 'mon_an'

    ma_mon = sqldb.Column(sqldb.Integer, primary_key = True)
    ten_mon = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    image = sqldb.Column(sqldb.String(255), nullable = False)
    cong_thuc = sqldb.Column(sqldb.Text, nullable = False)
    nguyen_lieu = sqldb.Column(sqldb.Text, nullable = False)
    ma_nl = sqldb.Column(sqldb.Integer, ForeignKey('thanh_phan.id'), nullable = True)
    ma_vh = sqldb.Column(sqldb.Integer, ForeignKey('van_hoa.id'), nullable = True)
    ma_cach_cb = sqldb.Column(sqldb.Integer, ForeignKey('cach_cb.id'), nullable = True)
    ma_mua = sqldb.Column(sqldb.Integer, ForeignKey('_mua.id'), nullable = True)
    video = sqldb.Column(sqldb.String(255), nullable = False)
    def __repr__(self):
        return "mon_an('{self.ten_mon}', '{self.image}', '{self.cong_thuc}', '{self.nguyen_lieu}', '{self.video}')"

class thanh_phan(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    id = relationship("mon_an", back_populates="ma_nl")
    def __repr__(self):
        return "thanh_phan('{self.id}', '{self.name}')"

class van_hoa(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    id = relationship("mon_an", back_populates="ma_vh")
    def __repr__(self):
        return "van_hoa('{self.id}', '{self.name}')"


class _mua(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    id = relationship("mon_an", back_populates="ma_mua")
    def __repr__(self):
        return "_mua('{self.id}', '{self.name}')"

class cach_cb(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    name = sqldb.Column(sqldb.String(255), unique = True, nullable = False)
    id = relationship("mon_an", back_populates="ma_cach_cb")
    def __repr__(self):
        return "cach_cb('{self.id}', '{self.name}')"
