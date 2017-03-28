# -*- coding: UTF-8 -*-
import pymongo
#创建一个客户端 ip，端口
client = pymongo.MongoClient('localhost',27017)
#给数据库命名
walden = client['walden']
#创建一个sheet页相当于表
sheet_line = walden['sheet_line']
sheet_tab = walden['sheet_tab']
# path ='D:\pythoncode\worm\walden.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         #一行一行读取并赋值出一个字典
#         data = {
#             'index':index,
#             'line':line,
#         'word':len(line.split())
#         }
#         #每次循环并把创建的data数据加进表中
#         sheet_tab.insert(data)

#查询表的数据

for item in sheet_tab.find({'word':{'$lt':5}}):
    print(item)


