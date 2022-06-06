#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2021/12/10 3:35 下午
# software: PyCharm
import json
import seldom

from test_dir.common.basic import get_filePath, get_config
from test_dir.common.log import Log
from test_dir.mmc_lilly.lilly_login import Login

log = Log()


class Send(seldom.TestCase):

    def setUp(self):
        self.url = get_config(name='lillyHost_test',key='url') + get_config(name='lilly_api',key='lilly_receive')
        self.send_data = get_filePath('test_data/mmc_lilly/send_data.json')
        self.receive_data = get_filePath('test_data/mmc_lilly/receive_data.json')
        self.headers = Login().headers
        self.headers['Cookie'] = Login().get_userAuth()

    def tearDown(self):
        log.info('---------- 测试结束 ----------\n')

    def test_01_send(self):
        '''
        发货接口
        :return:
        '''
        log.info('---------- 测试开始 ----------')
        log.info('接口地址：' + self.url)
        with open(self.send_data, 'r') as f:
            data = json.load(f)
        log.info('请求参数：' + str(data))
        self.post(self.url, json=data, headers=self.headers)
        self.assertStatusCode(200)
        log.info('响应参数：')
        log.info('响应参数：' + str(self.response))
        self.assertEqual(self.response['message'], 'success')

        #读取上一次收货json并对number和order_id更新
        with open(self.receive_data, 'r', encoding='utf-8') as f:
            receive_data = json.load(f)
            log.info('原运单号：'+ receive_data['number'])
            receive_data['number'] = self.response['data'][0]['number']
            log.info('最新运单号：'+ receive_data['number'])
            log.info('原order_id：'+ str(receive_data['order_id']))
            receive_data['order_id'] = self.response['data'][0]['order_id']
            log.info('最新order_id：'+ str(receive_data['order_id']))

            #写入最新的number和order_id
            with open(self.receive_data, 'w', encoding='utf-8') as f1:
                json.dump(receive_data, f1)
        log.info('---------- 测试通过 ----------\n')


if __name__ == '__main__':
    seldom.main()