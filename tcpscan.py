# -*- coding: UTF-8 -*-
import optparse
from socket import *
import threading
from threading import Thread
#socket
#设置个信号量
screenLock = threading.Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('test!')
        result = connSkt.recv(1024)
        connSkt.close()
        #加锁
        screenLock.acquire()
        print '[+] %d/tcp open ' % tgtPort
        print '[+] service: '+str(result)
    except:
        #加锁
        screenLock.acquire()
        print '[-] %d/tcp closed '% tgtPort
    finally:
        #无论如何最后都要释放这个锁和关闭连接
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        #connScan(tgtHost,int(tgtPort))
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()
#parse
def main():
    parse = optparse.OptionParser("usage %prog -H <target host> -P <target port>")
    parse.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parse.add_option('-P',dest='tgtPort',type='string',help='specify target port')
    (options,args) = parse.parse_args()
    if (options.tgtHost==None):
        print parse.usage
    elif (options.tgtPort==None):
        print 'use default port'
        tgtHost = options.tgtHost
        tgtPorts=[20,21,22,23,25,69,80,109,110,139,179,443,445,544,1080,1433,1434,1521,1158,2100,3306,3389,7001,8080,8081,9080,9090,8089,10050,27017,28017,5900]
        portScan(tgtHost,tgtPorts)
    else:
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')
        print tgtHost+':'+str(tgtPorts)
        portScan(tgtHost,tgtPorts)

if __name__ =='__main__':
    main()

