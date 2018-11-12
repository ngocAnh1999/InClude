import pymysql.cursors
from flask_api import FlaskAPI
from flask import request
app = FlaskAPI(__name__)

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='ngocanh1999',                             
                             db='sinhvien',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")


@app.route('/users/')
def getUsers():
    try:
        with connection.cursor() as cursor:
        
            sql = "SELECT ho, diemthi FROM sinhvienk60 "
            cursor.execute(sql)
            
            print ("cursor: ", cursor)

            print()

            users = []
            for row in cursor:
                user = {"ho": row['ho'], "diemthi": row['diemthi']}
                users.append(user)

                # return user  
            return users
            
    finally:
        connection.close()


    
if __name__ == '__main__':
    app.run()
