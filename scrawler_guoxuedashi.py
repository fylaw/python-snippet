#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from urllib import request
from urllib import error

from pyquery import PyQuery as pq

import os
import requests

baseUrl = 'http://shufa.guoxuedashi.com/%s/%s/' #抓取地址
shufa = '1' # 书法类型. 楷体
imgSuffix = '.png' # 图片类型后缀

start = 0x4e00
#end = 0x9fa5
end = 0x4e12

# 图片存放路径
basepath = os.path.join(os.path.abspath('.'),'guoxuedashi', shufa)
if not os.path.exists(basepath):
    os.makedirs(basepath)

# 日志存放路径
indexpath = os.path.join(basepath, 'index.txt')

# 日志级别:1=debug,2=info,3=warning,4=error
log_level = 2;

# 抓取指定字的图片
def retriveImg(index):
    code = hex(index).split('x')[1]
    info('get %s ...' % code)


    url = baseUrl % (code, shufa)
    with requests.get(url, timeout=5) as r:
        doc = pq(r.text)

        # 判断字是否存在
        # 存在时的html: <dl><dt><strong>【<a href="/4E00/1/" target="_blank">楷书书法</a>】</strong></dt></dl>
        # 不存在时的html: <dl><dt><strong>【热门查询】</strong></dt></dl>
        if not doc('dl a'):
            info('字%s不存在,跳过' % code)
            return

        # 建立每个字的目录
        tpath = os.path.join(basepath, code)
        if not os.path.exists(tpath):
            os.mkdir(tpath)

        # 编码对应的汉字
        the_font = doc('#sokeyshufa').attr('value')

        links = doc('table.table2 a')
        num = 0
        for link in links.items():
            #filename = link.text().encode('ISO-8859-1').decode('utf-8')

            src = link('img').attr('src')
            debug(src)
            try:
                debug('try to get image...')
                o = request.urlretrieve(src, os.path.join(tpath, str(num) + imgSuffix))
                debug(o)
                num = num + 1
            except error.URLError as e:
                log_error('met error when get image %s' % src)


def record(index):
    with open(indexpath, 'w') as f:
        f.write(str(index))

def log(level, message):
    if level >= log_level:
        print(message)

def debug(message):
    log(1, message)

def info(message):
    log(2, message)    

def warn(message):
    log(3, message)      

def log_error(message):
    log(4, message)  

if __name__ == '__main__':
    with open(indexpath, 'r') as f:
        start = int(f.read())
    info('starts from %s' % start)

    # 循环抓取每个字对应的图片
    for index in range(start, end):
        retriveImg(index)
        record(index)
