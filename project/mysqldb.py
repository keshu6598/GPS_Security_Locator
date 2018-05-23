import MySQLdb
conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "abhigya@1997",
                           db = "myflaskapp",
                           port=5000)
c=conn.cursor()
c.execute("SELECT * FROM users")
row = c.fetchall()
print(row)