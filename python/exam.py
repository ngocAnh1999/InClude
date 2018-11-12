import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%I %p %M %S %A %d %B %Y"))
# print(x.strftime(""))
from dateutil import parser

s = '2018-10-26T12:00:00.000+07:00'
dt = parser.parse(s)

# s = "2018-10-26T12:00:00.000+07:00"



# dateObj = datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f %Z")
print dt
