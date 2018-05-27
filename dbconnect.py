import MySQLdb
def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "987654321",
                           db = "project",
                          )
    c = conn.cursor()

    return c, conn
