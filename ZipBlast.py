# -*- coding: UTF-8 -*-
import zipfile
import optparse
from threading import Thread

#解压方法，传入压缩文件和密码
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password '+password + '\n'
    except:
        pass
#主方法，主要用optparse来格式化参数和获取参数。并线程调用解压方法
def main():
    #这个是如果不输入参数就会显示下面这个
    parser = optparse.OptionParser("usage%prog "+"-f <zipfile> -d <dictionary>")
    #设置对应的参数
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dictonary file')
    #获取参数
    (options,args)= parser.parse_args()
    #如果参数为空
    if(options.zname==None)|(options.dname==None):
        print parser.usage
        exit(0)
    else:
        #将参数获取的值赋值
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        #去除每行后面的换行符
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile,password))
        t.start()
if __name__ =='__main__':
    main()





