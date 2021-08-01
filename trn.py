import socket

r = socket.socket()

host = socket.gethostname()

port = 8080

r.bind ((host,port))

r.listen(1)

print ("Your Key Send To Admin If Admin Online")

print ("")

print (host)

print ("")

print ("wait for admin perrmison")

conn, addr=r.accept()

print ("Admin Give Green Single")

file=open("vxt.txt",'rb')

file_data=file.read(1024)

conn.send(file_data)

print ("Now You Have Permison to Login")
