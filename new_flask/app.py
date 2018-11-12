from flask_api import FlaskAPI
from flask import request
app = FlaskAPI(__name__)

users = [
        {"name": "Anh", "year": 1999},
        {"name": "Anhbeo", "year": 1999}
    ]

@app.route('/users')
def helloWorld():
    
    return users

@app.route('/users/<x>/')
def getUserByName(x):
    for user in users:
        if x == user['name']:
            return user 
    return {
        "message": "Not found"
    }
    
    
if __name__ == '__main__':
    app.run()
