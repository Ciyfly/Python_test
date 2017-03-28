# -*- coding: utf-8 -*-
import codecs
import random
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
import jieba.analyse
with open('ci.txt','r') as f:
    seg_list =jieba.analyse.extract_tags(f.read(), topK=20, withWeight=True, allowPOS=())
wd={}
for tag in seg_list:
        wd[tag[0]] = float(tag[1])
from operator import itemgetter
swd = sorted(wd.iteritems(), key=itemgetter(1), reverse=True)
tags = make_tags(swd,minsize = 50, maxsize = 240,colors=random.choice(COLOR_SCHEMES.values()))
create_tag_image(tags, 'yun.png', background=(0, 0, 0, 255),
size=(2400, 1000),layout=LAYOUT_HORIZONTAL,
fontname="SimHei")
