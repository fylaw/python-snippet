# -*- coding:utf8 -*-
import os
import re
import requests as rq
import urllib
import time

cp = os.path.abspath('.')
ap = os.path.join(cp, 'images')
if not os.path.exists(ap):
    os.mkdir(ap)
os.chdir(ap)

for index in range(1, 72):
    urllib.request.urlretrieve('http://img.docin.com/huangke/dfs_store_001/api/1360850505/image/bg_0_%s.jpg' % index, 'bg_0_%s.jpg' % index)


#res = urllib.request.urlretrieve('http://img.docin.com/huangke/dfs_store_001/api/1360850505/image/bg_0_1.jpg')
#print(res)