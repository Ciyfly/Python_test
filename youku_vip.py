# -*- coding: UTF-8 -*-
#../code.php?s=992671249
#url='http://vip.cengfan6.com/y/'
import requests
from bs4 import BeautifulSoup
import random
from PIL import Image
import time
import re
#获取验证码
def getyzm():
    headers={
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    #Cookie:PHPSESSID=d763fd34e25925880c490955de8e0f2c
    'Host':'vip.cengfan6.com',
    'Referer':'http://vip.cengfan6.com/y/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }
    i =random.randint(1,999999)
    print(i)
    url='http://vip.cengfan6.com/y/../code.php?s=%i' %i
    html = requests.get(url,headers=headers)
    #写出图片
    with open('yzm.png','wb') as f:
        f.write(html.content)

#识别验证码
def viewyzm():
    print('please input yanzhengma')
    time.sleep(2)
    image = Image.open('yzm.png')
    image.show()
    yzm = raw_input(u'关闭图片才能输入')
    return yzm



xhrhd ='''
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Cookie:PHPSESSID=d3a9d9a7a9ad9fee71a9588773388ead
Host:vip.cengfan6.com
Referer:http://vip.cengfan6.com/y/
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36
X-Requested-With:XMLHttpRequest
'''


def  get_vip():
    #请求，但是没有解密，可以在历史记录中获取获取到的vip账号
    headers={
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'PHPSESSID=d3a9d9a7a9ad9fee71a9588773388ewd',
    'Host':'vip.cengfan6.com',
    'Referer':'http://vip.cengfan6.com/y/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }
    proxies={
        '117.90.6.65':9000
    }
    vip_url='http://vip.cengfan6.com/ajax.php?code=%s &typename=2' %viewyzm()
    viphtml  = requests.get(vip_url,headers=headers,proxies=proxies)
    print(viphtml.content)
def get_host_vip():
    proxies={
        '117.90.6.65':9000
    }
    vip_url= 'http://vip.cengfan6.com/ajax_jilu.php?viptype=2'
    viphtml  = requests.get(vip_url,proxies=proxies)
    vips =re.findall('<p>优酷（土豆）帐号：(.+?)密码：(.+?)</p>',viphtml.content)
    for vip in vips:
        print(vip[0]+":"+vip[1])
getyzm()
get_vip()
get_host_vip()









