#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/7/12 2:15 下午
# software: PyCharm
"""
    用户反馈接口
"""
import unittest

import pandas as pd
from parameterized import parameterized

from test_dir.mmc_bigapp.BigApp_basic import BigAppBasic
from test_dir.common.basic import get_config, list_outputExcelInfo, get_filePath


class BigAppFeedBack(unittest.TestCase):

    #### 引入测试数据 DDT 驱动
    jsonData = pd.read_excel(get_filePath("test_data/mmc_bigapp/bigapp_testdata.xls"), sheet_name="用户反馈")
    # print(jsonData)
    testData = jsonData.values.tolist()
    # print(testData)

    def setUp(self):
        self.hearders = BigAppBasic().headers
        self.se = BigAppBasic().se
        self.warning = BigAppBasic().warning
        self.feedBackUrl = BigAppBasic().host + get_config(name='bigAppHost', key='bigApp_feedback')
        self.log = BigAppBasic().log
        # self.testData = list_outputExcelInfo(dataPath=get_filePath("test_data/mmc_bigapp/bigapp_testdata.xls"), sheetNane='用户反馈', startRow=0, startCol=0)

    def tearDown(self):
        self.log.info('---------- 测试结束 ----------\n')

    @parameterized.expand(testData)
    def test_getBasicInfo(self, testData, assertStatusCode, assertData):
        """
        用户反馈接口测试
        :return:
        """
        self.log.info('---------- 测试开始 ----------')
        self.log.info('接口地址：' + self.feedBackUrl)
        self.log.info('请求参数：' + str(testData))
        resp = self.se.post(url=self.feedBackUrl, headers=self.hearders, json=testData)
        self.assertEqual(resp.status_code, assertStatusCode, msg="服务器响应码"+str(resp.status_code))
        self.log.debug('响应参数：' + str(resp.json()))
        self.assertEqual(resp.json()['code'], assertData, msg="接口返回信息错误，请检查"+ str(resp.json()))
        print('\n')


if __name__ == '__main__':
    unittest.main()