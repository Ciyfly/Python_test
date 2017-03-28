# -*- coding: UTF-8 -*-
import ftplib
import optparse
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','Recar@Recar.com')
        print '\n[*] '+str(hostname) + ': FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception,e:
        print '\n[-] '+str(hostname)+': FTP Anonymous Logon Failed.'
        return False

def main():
    parse = optparse.OptionParser("usage %prog -H <target host>")
    parse.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    (options,args) = parse.parse_args()
    if (options.tgtHost==None):
        print parse.usage
    else:
        host=options.tgtHost
        anonLogin(host)
if __name__=='__main__':
    main()