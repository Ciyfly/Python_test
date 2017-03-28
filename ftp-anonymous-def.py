# -*- coding: UTF-8 -*-
import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','Recar@Recar.com')
        print '\n[*]'+str(hostname) + 'FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception,e:
        print '\n[-]'+str(hostname)+'FTP Anonymous Logon Failed.'
        return False
host = '192.168.150.137'
anonLogin(host)





