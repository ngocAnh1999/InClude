#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl, requests, pymysql
from app_project import conn


cursor = conn.cursor()


path = "/home/ngocanh/Downloads/DatabaseCongthucnauan.xlsx"
sql_1 = "SELECT * from cach_cb"
cursor.execute(sql_1)
results = cursor.fetchall()
wb = openpyxl.load_workbook(path)
sheet = wb.get_sheet_by_name("Bang_cach_che_bien")
# print(len(results))
# max_row = sheet_monan.max_row

for i in range(0, len(results)):
    
    for j in range(0, len(results[i])):
        cell = sheet.cell(row = i+2, column = j+1)
        cell.value = results[i][j]

wb.save(path)
        
conn.close()