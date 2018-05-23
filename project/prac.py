from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from dbconnect import connection

import MySQLdb

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])

def index():
    if request.method == 'POST':
       userDetails = request.form
       name = userDetails['name']
       email = userDetails['email']
       c, conn = connection()
       c.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name,email))
       conn.commit()
       c.close()
       conn.close()
       c, conn = connection()
       c=conn.cursor()
       c.execute("SELECT * FROM users")
       data = c.fetchall()
       print(data)
       return 'sjksdvhlsav'
    return render_template('index.html')

if __name__=='__main__':
   app.run(debug=True)

