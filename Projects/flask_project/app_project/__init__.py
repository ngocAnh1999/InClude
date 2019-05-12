from db import connection
from api import sqldb
from elasticsearch import Elasticsearch
from models import Mon_an, Thanh_phan, Van_hoa, Cach_cb, _mua, Meovaobep, Meovat

mon_an = Mon_an
thanh_phan = Thanh_phan
van_hoa = Van_hoa
cach_cb = Cach_cb
mua = _mua
meovaobep = Meovaobep
meovat = Meovat

sqldb = sqldb
conn = connection()