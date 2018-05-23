from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abhigya@1997'
app.config['MYSQL_DB'] = 'myflaskapp'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])

def index():
    if request.method == 'POST':
       userDetails = request.form
       name = userDetails['name']
       email = userDetails['email']
       cur = mysql.connection.cursor()
       cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name,email))
       mysql.connection.commit()
       cur.close()
       return 'akfgilsdgvc;ouegfrf'
    return render_template('index.html')

if __name__=='__main__':
   app.run(debug=True)

