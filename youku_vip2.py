# -*- coding: UTF-8 -*-
#../code.php?s=992671249
#url='http://vip.cengfan6.com/ajax_jilu.php?viptype=2'
#608282c72cb6e2b8e83487d4d426d4a2
import requests
from PIL import Image
import time
import re
#re  code2016|s|afc769ff349d70b5dab9085b28498bce|code2016
#http://vip.cengfan6.com/ajax.php?code=6852&typename=2
regex ='code2016(.+?)\|code2016'

headers={
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'PHPSESSID=d3a9d9a7a9ad9fee71a9588773388ewd',
        'Host':'vip.cengfan6.com',
        'Referer':'http://vip.cengfan6.com/y/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'X-Forwarded-For':'222.247.85.51'
        }

#将账号密码显示出来
def get_host_vip():

    vip_url= 'http://vip.cengfan6.com/ajax_jilu.php?viptype=2'
    viphtml  = requests.get(vip_url)
    vips =re.findall('<p>优酷（土豆）帐号：(.+?)密码：(.+?)</p>',viphtml.content)
    for vip in vips:
        print(vip[0]+":"+vip[1])

#识别验证码
def viewyzm():
    print('please input yanzhengma')
    time.sleep(2)
    image = Image.open('yzm.png')
    print(u'关闭图片才能输入')
    image.show()
    yzm = raw_input()
    return yzm

def huoquyzm():
    url='http://vip.cengfan6.com/y/'

    html = requests.get(url,headers=headers)
    yzm1 =  re.findall(regex,html.content)
    for yz in yzm1:
        yzm = yz.split('|')[2]
        url2 = 'http://vip.cengfan6.com/code2016.php?s=%s' %yzm
        print(url2)
        html2 = requests.get(url2,headers=headers)
        #写出图片
        with open('yzm.png','wb') as f:
            f.write(html2.content)
#进行获取验证码，人工识别，再次请求获取账号密码
huoquyzm()
csyzm =viewyzm()
url3 ='http://vip.cengfan6.com/ajax.php?code=%s&typename=2' %csyzm

html3 = requests.get(url3,headers=headers)
print(html3.content)
get_host_vip()

