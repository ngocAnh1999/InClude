import sys
import math
import random
import time
import calendar
print calendar.prmonth(2018,12)

localtime = time.localtime(time.time())
localtime = time.asctime(localtime)
print "Thoi gian hien tai la :", localtime
time.sleep(1)
print "time.ctime() : %s" % time.ctime()
print time.tm_mday()
# n = 5
# for index in range(0, n) :
#     print index , " "
# print abs(-2)
# print math.ceil(-2.3)
# print cmp(20, 10)
# print math.exp(2)
# print math.floor(32.33)
# print math.modf(22.23)
# x = 2 ; y = 3
# print math.pow(y, x)
# print round(22.242324, 2)
# print math.sqrt(4)
# var1 = "anh is master"
# print var1[0]
# print var1[0:3]
# print var1.capitalize()
# print var1.center(21, '*')
# var2 = "s"
# print "so luong chu %s trong var1 la %d" % (var2, var1.count(var2, 0, len(var1)))
# print random.randrange(2, 4, 3)
# print random.uniform(2, 4)
# var1 = var1.encode('base64', 'strict')
# print "chuoi ma hoa la " , var1
# print "giai ma " , var1.decode('base64', 'strict')
# var3 = "1234"
# print "%s la mot so phai khong : %s" % (var3, var3.isdigit())
# aList = [123, 'xyz', 'hoang', 'abc'];

# print "A List : ", aList.pop()
# print "B List : ", aList.pop(1)
# print aList