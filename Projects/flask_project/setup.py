#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl, requests, pymysql
# from app_project import conn

def connection():
        host = "localhost"
        user = "root"
        password = "yourpassword" #--> thay password của bạn vào đây
        dbname = "your_database" #--> thay tên database bạn sẽ thao tác với nó vào đây
        db = pymysql.connect(host, user, password, dbname)
        return db

if __name__ == "__main__":
        # cursor = conn.cursor()
        cursor = connection().cursor()

        #--> thay đường dẫn path trỏ đến file excel bạn sẽ xuất data trong máy tính , 
        # trước đấy phải tạo 1 file excel trên máy, lưu lại, rồi copy đường dẫn vào đây
        path = "/home/ngocanh/Downloads/DatabaseCongthucnauan.xlsx"

        # --> thay tên bảng mà bạn muốn xuất ra excel
        table_name = "cach_cb"
        sql_1 = "SELECT * from {}".format(table_name)
        cursor.execute(sql_1)
        results = cursor.fetchall()
        wb = openpyxl.load_workbook(path)

        #--> thay tên của sheet mà bạn muốn export (đổi tên sheet cho phù hợp)
        #  trước đó phải tạo 1 sheet trống, 
        # dòng đầu tiên của sheet bạn tự viết tên các cột theo thứ tự của cột như trong bảng table_name
        sheet = wb.get_sheet_by_name("Bang_cach_che_bien")  

        for i in range(0, len(results)):
        
                for j in range(0, len(results[i])):
                        cell = sheet.cell(row = i+2, column = j+1)
                        cell.value = results[i][j]

        wb.save(path)
                
        conn.close()
        # --> sau khi thay xong , thực hiện các lệnh sau:.
        # đầu tiên mở môi trường ảo : source venv/Scripts/activate 
        # nếu chưa cài các thư viện openpyxl, requests, pymysql thì dùng pip để cài:
        # pip install openpyxl (tương tự với các thư viện còn lại)
        # cuối cùng runfile: python setup.py

        # sudo apt install python3-pip
        # pip3 install --user pipenv
        # pipenv --python 3.7