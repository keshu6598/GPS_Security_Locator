from dbconnect import connection
import MySQLdb
from flask_mysqldb import MySQL
import datetime
class Device:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng
def storedata(data):
       longitude = data.lng
       latitude = data.lat
       imeino = data.name
       
       c, conn = connection()
       c.execute("INSERT INTO datas(imei_no, registration_no,latitude,longitude) VALUES(%s, %s, %s,%s)",(imeino,123,latitude,longitude))
       conn.commit()
       c.close()
       conn.close()
