from flask_mysqldb import MySQL
from dbconnect import connection
from seperation_ofinputdata import seperation
from storedata import storedata
import MySQLdb
import socket 
class Device:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

s = socket.socket()
print("Socket successfully created")

port=4001
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.110.90',port))
print('socket binded to %s' %(port))
s.listen(5)
print('socket is listening')

while True :
   try:
   	a, addr = s.accept()
   	print('got connection from', addr)
   	output = a.recv(8192)
   	if output:
   		if(len(str(output))>=61):
     			try:
     				print("data recived", str(output))
     				data = Device("",0.0,0.0)
     				data = seperation(str(output))
     				storedata(data)
     			except:
     				pass	
   	a.close()
   except KeyboardInterrupt:
   	s.close()	
   