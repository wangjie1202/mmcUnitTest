#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/7/12 1:55 下午
# software: PyCharm
"""
    获取app基本信息
"""
import unittest
from test_dir.mmc_bigapp.BigApp_basic import BigAppBasic
from test_dir.common.basic import get_config


class BigAppBasicInfo(unittest.TestCase):

    def setUp(self):
        self.headers = BigAppBasic().headers
        self.se = BigAppBasic().se
        self.warning = BigAppBasic().warning
        self.basicInfoUrl = BigAppBasic().host + get_config(name='bigAppHost', key='bigApp_getBasicInfo')
        self.log = BigAppBasic().log

    def tearDown(self):
        self.log.info('---------- 测试结束 ----------\n')

    def test_getBasicInfo(self):
        self.log.info('---------- 测试开始 ----------')
        self.log.info('接口地址：' + self.basicInfoUrl)
        resp = self.se.post(url=self.basicInfoUrl, headers=self.headers)
        print(resp)


if __name__ == '__main__':
    unittest.main()