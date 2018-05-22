
import socket 
s = socket.socket()
print("Socket successfully created")

port=4001
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.110.90',port))
print('socket binded to %s' %(port))
s.listen(5)
print('socket is listening')

while True :
   file=open("write.txt","w")
   c, addr = s.accept()
   print('got connection from', addr)
   output = c.recv(8192)
   if output:
     print("data recived", str(output))
  
     file.write("/n" + str(output))
   c.close()
   file.close()   
