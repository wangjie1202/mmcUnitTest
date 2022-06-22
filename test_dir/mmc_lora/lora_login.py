#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2021/12/10 2:06 下午
# software: PyCharm
import re

import requests

from test_dir.common.basic import get_filePath, get_config

'''
lora登录接口
'''


class Login():

    def __init__(self):
        self.url = get_config(name='loraHost_online', key='url') + get_config(name='lora_api', key='lora_Login')
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.se = requests.Session()
        self.userAuth = get_filePath("test_data/mmc_lora/user_auth.txt")

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
        data = {"password": "gs1234", "username": "gs"}
        res = self.se.post(url=self.url, headers=self.headers, json=data)
        # print(res.headers)

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