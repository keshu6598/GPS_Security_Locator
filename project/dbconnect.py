import MySQLdb
def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "abhigya@1997",
                           db = "myflaskapp",
                           port=5000)
    c = conn.cursor()

    return c, conn
