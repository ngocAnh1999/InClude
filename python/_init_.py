#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fo = open("diction.txt", "r")
# print "Ten cua file la: ", fo.name
# print "File da duoc dong hay chua : ", fo.closed
# print "Che do mode la : ", fo.mode
# print "Softspace la : ", fo.softspace
# s = fo.read()
# print s
# fo.close()
try:
   fh = open("diction.txt", "a")
   fh.write("\nDay la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print "Error: Khong tim thay file"
else:
   print "Thanh cong ghi noi dung vao file"
   fh.close()
try:
    fo = open("diction.txt", "r")
    print fo.read()
except IOError:
    print "ERROR : không tìm thấy file"
else:
    print "Đọc file thành công"
    fo.close()