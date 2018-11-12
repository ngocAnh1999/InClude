import json

import requests
data = requests.get("http://localhost:5000/users/Anh")
jsonDt = data.json()
# with open('test.json') as data_file:    
#     data = json.load(data_file)
# s = "2/10/2018"
# date = parser.parse(s)
# for x in data:
#     time = parser.parse(x["thoi gian"])
#     if (time == date) :
#         pprint(x["hoat dong"])
print jsonDt