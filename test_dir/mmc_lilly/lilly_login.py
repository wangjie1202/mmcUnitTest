#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2021/12/10 2:06 下午
# software: PyCharm
import re
import warnings

import requests

from test_dir.common.basic import get_filePath, get_config

'''
app登录接口
'''


class Login():

    def __init__(self):
        self.url = get_config(name='lillyHost_online', key='url') + get_config(name='lilly_api', key='lilly_AppLogin')
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.se = requests.Session()
        self.userAuth = get_filePath("test_data/mmc_lilly/user_auth.txt")
        self.warning = warnings.simplefilter("ignore", ResourceWarning)

    def get_userAuth(self):
        '''
        读取cookie
        :return: cookie
        '''
        with open(self.userAuth) as f:
            cookie = f.read()
        return cookie

    def login(self):
        '''
        TODO
        app端登录获取cookie
        :return:
        '''
        data = {"password":"mxd12345","username":"mxd"}
        res = self.se.post(url=self.url, headers=self.headers, json=data)

        #正则提取csrftoken和sessionid
        temp = res.headers['Set-Cookie']
        csrftoken = re.findall('csrftoken=(.*?); expires', temp)
        csrftoken = csrftoken[0]
        sessionid = re.findall('sessionid=(.*?); expires=', temp)
        sessionid = sessionid[0]

        #写入cookie
        with open(self.userAuth, 'w') as f:
            f.write('csrftoken='+csrftoken+';sessionid='+sessionid)
        self.se.close()
        return '登录成功'


if __name__ == '__main__':
    print(Login().login())