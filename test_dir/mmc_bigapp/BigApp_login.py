#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/7/12 2:59 下午
# software: PyCharm


"""
    用户登录接口
"""
import json
import unittest

from parameterized import parameterized

from test_dir.mmc_bigapp.BigApp_basic import BigAppBasic
from test_dir.common.basic import get_config, list_outputExcelInfo, get_filePath


class BigAppLogin(unittest.TestCase):

    testData = list_outputExcelInfo(dataPath=get_filePath("test_data/mmc_bigapp/bigapp_testdata.xls"), sheetNane='用户登录',
                                    startRow=0, startCol=0)

    def setUp(self):
        self.hearders = BigAppBasic().headers
        self.se = BigAppBasic().se
        self.warning = BigAppBasic().warning
        self.userLoginUrl = BigAppBasic().host + get_config(name='bigAppHost', key='bigApp_login')
        self.log = BigAppBasic().log
        # self.testData = list_outputExcelInfo(dataPath=get_filePath("test_data/mmc_bigapp/bigapp_testdata.xls"), sheetNane='用户登录', startRow=0, startCol=0)

    def tearDown(self):
        self.log.info('---------- 测试结束 ----------\n')

    @parameterized.expand(testData)
    def test_userLogin(self, testData):
        """
        用户登录接口测试
        :return:
        """
        self.log.info('---------- 测试开始 ----------')
        self.log.info('接口地址：' + self.userLoginUrl)
        self.log.info('请求参数：' + str(testData))
        resp = self.se.post(url=self.userLoginUrl, headers=self.hearders, data=testData)
        self.log.debug('response code：' + str(resp.status_code))
        self.assertEqual(resp.status_code, 200, msg="服务器响应码"+str(resp.status_code))
        self.log.debug('响应参数：' + str(resp.json()))
        self.assertEqual(resp.json()['message'], 'login success', msg="接口返回信息错误，请检查" + str(resp.json()))
        print('\n')


if __name__ == '__main__':
    unittest.main()