#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python
# import pymysql.cursors
from flask_api import FlaskAPI
# from flask import request as flask_request
app = FlaskAPI(__name__)
import requests
# import json
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
@app.route("/cgi")
def requestCGI():
    # Get data from fields
    if form.getvalue('maths'):
        math_flag = "ON"
    else:
        math_flag = "OFF"

    if form.getvalue('physics'):
        physics_flag = "ON"
    else:
        physics_flag = "OFF"

    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Checkbox - Third CGI Program</title>"
    print "</head>"
    print "<body>"
    print "<h2> CheckBox Maths is : %s</h2>" % math_flag
    print "<h2> CheckBox Physics is : %s</h2>" % physics_flag
    print "</body>"
    print "</html>"
if __name__ == '__main__':
    app.run()
