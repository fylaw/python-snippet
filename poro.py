# -*- coding:utf8 -*-

# poro的每日签到

import sys, io
import urllib.request
import http.cookiejar


hostname = 'http://poro.fun'

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') # 改变标准输出的默认编码

def checkin(user):

    # 登录时要提交的数据
    data = {
        'email': user['email'],
        'passwd': user['passwd'],
        'remember_me': 'week'
    }
    post_data = urllib.parse.urlencode(data).encode('utf-8')

    # 设置请求头
    headers = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 登录请求地址
    login_url = hostname + '/auth/login'

    #构造登录请求
    req = urllib.request.Request(login_url, headers=headers, data=post_data)

    # 构造cookie
    cookie = http.cookiejar.CookieJar()

    # 由cookie构造opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    response = opener.open(req)

    # 登录后才能访问的页面
    url = hostname + '/user/checkin'

    req = urllib.request.Request(url, headers=headers, data={})
    response = opener.open(req)
    print(response.read().decode('unicode_escape'))

users = [{'email':'user1', 'passwd':'passwd1'}, {'email':'user2', 'passwd':'passwd2'}]
for user in users:
    checkin(user)