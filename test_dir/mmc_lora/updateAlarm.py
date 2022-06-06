#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/5/18 10:19 上午
# software: PyCharm
import warnings
import requests
import json
import unittest

from test_dir.mmc_lora.lora_login import Login

"""
lora后台，处理报警中心的报警消息；
"""


class Lora_USA(unittest.TestCase):

    def setUp(self):
        self.headers = Login().headers
        self.headers['Cookie'] = Login().get_userAuth()
        self.se = requests.Session()
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        pass

    def test_updateAlarm(self):
        '''
        获取报警中心报警数量并完成处理
        :return:
        '''
        url = "http://na.lora.zenm.vip/iot/lora/get/event/?page=1&type=0"
        response = self.se.get(url=url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        resp_data = response.json()['data']

        if(len(resp_data)<1):
            print("没有要处理的警情！")
        else:
            print("待处理报警共（条）：", len(resp_data))
            for i in range(0, len(resp_data)):
                id_data = resp_data[i]['id']
                url_1 = "http://na.lora.zenm.vip/iot/lora/update/event/"
                data = {"id": id_data}
                response_1 = self.se.post(url=url_1, headers=self.headers, json=data)
                self.assertEqual(response.status_code, 200)
                print(response_1.json())
            print("处理完成！")


if __name__ == '__main__':
    unittest.main()

