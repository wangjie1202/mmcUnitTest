#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2021/12/10 2:26 下午
# software: PyCharm
import json
import seldom

from test_dir.common.basic import get_filePath, get_config
from test_dir.common.log import Log
from test_dir.mmc_lilly.lilly_login import Login

log = Log()


class Receive(seldom.TestCase):

    def setUp(self):
        self.url = get_config(name='lillyHost_test',key='url') + get_config(name='lilly_api',key="lilly_receive")
        self.receive_data = get_filePath('test_data/mmc_lilly/receive_data.json')
        self.headers = Login().headers
        self.headers['Cookie'] = Login().get_userAuth()

    def tearDown(self):
        log.info('---------- 测试结束 ----------\n')

    def test_01_receive(self):
        '''
        收货接口
        :return: None
        '''
        log.info('---------- 测试开始 ----------')
        log.info('接口地址：' + self.url)
        with open(self.receive_data, 'r') as f:
            data = json.load(f)
        log.info('请求参数：' + str(data))
        self.post(self.url, json=data, headers=self.headers)
        self.assertStatusCode(200)
        log.info('响应参数：' + str(self.response))
        self.assertEqual(self.response['message'], 'success')
        log.info('---------- 测试通过 ----------\n')


if __name__ == '__main__':
    seldom.main()