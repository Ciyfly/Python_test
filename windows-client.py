#!/usr/local/bin/python
from socket import *
from time import ctime
def main():
	HOST='127.0.0.1'
	PORT = 2333
	BUFSIZE=1024

	ADDR = (HOST,PORT)

	tcpServer = socket(AF_INET,SOCK_STREAM)
	tcpServer.bind(ADDR)
	tcpServer.listen(5)

	while True:
		try:
			print 'wait for connection...'
			tcpClient,addr = tcpServer.accept()
			print '..connected from :'+str(addr)
			while True:
				data = raw_input('~:')
				if data=='quit':
					tcpClient.close()
					tcpServer.close
				if data != "":
					tcpClient.send(data)
					data = tcpClient.recv(BUFSIZE)
					if not data:
						break
					print data.decode('gbk').encode('utf-8')
				
		except:
			pass
	tcpClient.close()
	tcpServer.close
if __name__ == '__main__':
	main()