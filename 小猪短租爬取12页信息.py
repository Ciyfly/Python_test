# -*- coding: UTF-8 -*-
#小猪短租爬取
import requests
from bs4 import BeautifulSoup
import json
def get_xinxi(i):
    url = 'http://cd.xiaozhu.com/search-duanzufang-p%d-0/' %i
    html = requests.get(url)
    soup = BeautifulSoup(html.content)
    #获取地址
    dizhis=soup.select(' div > a > span')
    #获取价格
    prices = soup.select(' span.result_price')
    #获取简单信息
    ems = soup.select(' div > em')
    datas =[]
    for dizhi,price,em in zip(dizhis,prices,ems):
        data={
            '价格':price.get_text(),
            '信息':em.get_text().replace('\n','').replace(' ',''),
            '地址':dizhi.get_text()
        }
        print(json.dumps(data).decode("unicode-escape"))
i=1
while(i<12):
    get_xinxi(i)
    i=i+1
