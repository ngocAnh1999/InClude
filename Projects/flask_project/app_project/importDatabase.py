#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from models import Mon_an, Thanh_phan, Van_hoa, Cach_cb, _mua
import openpyxl, requests, pymysql
from api import sqldb
path = "/home/ngocanh/Downloads/DatabaseCongthucnauan.xlsx"

def importMon_an():
        wb = openpyxl.load_workbook(path)
        sheet = wb.get_sheet_by_name("Bang_mua_dip_le")
        max_col = sheet.max_column
        max_row = sheet.max_row
        # print str(max_col) + " "+ str(max_row)
        for i in range(0, max_row - 1):
                # cell_id = sheet.cell(row = i+2, column = 1)
                cell = sheet.cell(row = i+2, column = 2)
                mua = _mua(cell.value.encode('utf-8'))
                # mua.setValue(cell.value.encode('utf-8'))
                sqldb.session.add(mua)
                sqldb.session.commit()

                
importMon_an()