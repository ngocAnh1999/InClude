import pymysql.cursors
from flask_api import FlaskAPI
from flask import request
app = FlaskAPI(__name__)

def getConnection():
    connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='ngocanh1999',                             
                                db='sinhvien',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful!!")
    return connection

@app.route('/users/')
def getUsers():
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
        
            sql = "SELECT ten, hocphi FROM hocphik60"
            cursor.execute(sql)
            
            print ("cursor: ", cursor)

            print()

            users = []
            for row in cursor:
                user = {"ten": row['ten'], "hocphi": row['hocphi']}
                users.append(user)

                # return user  
            return users
            
    finally:
        connection.close()

@app.route("/users/<name>/")
def getUserByName(name):
    connection = getConnection()
    try:
        with connection.cursor() as cursor:
        
            sql = "SELECT ten, hocphi FROM hocphik60"
            cursor.execute(sql)
            
            print ("cursor: ", cursor)

            print()

            users = []
            for row in cursor:
                user = {"ten": row['ten'], "hocphi": row['hocphi']}
                if name == user['ten'] :
                    users.append(user)
            
                # return user  
            return users

            
    finally:
        connection.close()

    
if __name__ == '__main__':
    app.run()
