#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/4/22 4:08 下午
# software: PyCharm
"""
大app公共参数
"""
import warnings
import requests
from test_dir.common.basic import get_config, get_filePath
from test_dir.common.log import Log


class BigAppBasic():

    def __init__(self):
        self.warning = warnings.simplefilter("ignore", ResourceWarning)
        self.headers = {"Content-Type": "application/json"}
        self.se = requests.Session()
        self.host = get_config(name='bigAppHost', key='url')
        self.userLoginUrl = self.host + get_config(name='bigAppHost', key='bigApp_login')
        self.userAuth = get_filePath("test_data/mmc_bigapp/user_auth.txt")
        self.log = Log()

    def get_userToken(self):
        '''
        读取token
        :return: token
        '''
        with open(self.userAuth) as f:
            token = f.read()
        return token

    def login(self):
        '''
        登录操作
        :return: 登录状态
        '''
        testData = {"username":"wj1234","password":"abcd1234"}
        resp = self.se.post(url=self.userLoginUrl, headers=self.headers, json=testData)
        if resp.status_code==200 and resp.json()['code']==0:
            token = resp.json()['data']['token']
            with open(self.userAuth, 'w') as f:
                f.write('token ' + token)
            self.se.close()
            return '登录成功'
        else:
            return '登录失败'


if __name__ == '__main__':
    print(BigAppBasic().login())






