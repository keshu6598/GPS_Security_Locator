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
       test = 75.187254
       idd = 2
       c, conn = connection()
       c.execute("""UPDATE datas SET name = %s, email = %s, test = %s where id= %s""",(name,email,test,idd))
       conn.commit()
       c.close()
       conn.close()
       c, conn = connection()
       c=conn.cursor()
       c.execute("SELECT * FROM user LIMIT 3")
       data = c.fetchall()
       print(data)
       return 'sjksdvhlsav'
    return render_template('index.html')

if __name__=='__main__':
   app.run(debug=True)

