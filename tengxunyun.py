# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.qcloud.com/act/campus'

def shijian():
    html = requests.get(url)
#weikaishi='#discount > div > div.toolbar > button' .data-title

    soup = BeautifulSoup(html.content)
    button = soup.select('#discount > div > div.toolbar > button')
    if button[0].text ==u'未开始':
        print('时间未到，未开始....')
    else:
        i=1
        huoqu()

def huoqu():
    headers={

    }
    url=''


i=0
while i==0 :
    shijian()
    time.sleep(2)

