#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/6/15 4:41 下午
# software: PyCharm
import unittest

from test_dir.common.basic import get_config, get_filePath
from test_dir.common.log import Log
from test_dir.mmc_lenglian.lengllian_login import Login

log = Log()


class Send(unittest.TestCase):

    def setUp(self):
        self.getDevRegTimeUrl = get_config(name='lenglianHost_online',key='url') + get_config(name='lenglian_api',key='lenglian_DevRgeTime')
        self.headers = Login().headers
        self.se = Login().se
        self.headers['Cookie'] = Login().get_userAuth()
        Login().warning

    def tearDown(self):
        log.info('---------- 测试结束 ----------\n')

    def test_getDevicesRegInfo(self):
        """
        TODO
        获取设备的注册时间
        :return:
        """
        log.info('---------- 测试开始 ----------')
        log.info('接口地址：' + self.getDevRegTimeUrl)
        page_data = "?page=1&type=0"
        log.info('请求参数：' + str(page_data))
        devices_resp = self.se.get(self.getDevRegTimeUrl + page_data, headers=self.headers)
        self.assertEqual(devices_resp.status_code, 200)
        self.assertEqual(devices_resp.json()['result'], 200)
        num_pages = devices_resp.json()['num_pages']
        resp_dataList = devices_resp.json()['data']
        log.info('请输入要查询的设备ID：')
        mmcId = input()

        # 遍历第一页的mmcid
        for i in range(0, len(resp_dataList)):
            sn = resp_dataList[i]['SN']
            if(mmcId==sn):
                create_time = resp_dataList[i]['create_time']
                log.info(mmcId + ' 的创建时间是：'+ create_time)
                return

            # 如果不在第一页，就往下继续请求
            elif(i+1 == len(resp_dataList)):
                log.warning('第1页未没有找到\n')
                for i in range(2, num_pages+1):
                    page_data = "?page=" + str(i) +"&type=0"
                    log.info('请求参数：' + str(page_data))
                    devices_resp = self.se.get(self.getDevRegTimeUrl + page_data, headers=self.headers)
                    resp_dataList = devices_resp.json()['data']
                    for j in range(0, len(resp_dataList)):
                        sn = resp_dataList[j]['SN']
                        if (mmcId == sn):
                            create_time = resp_dataList[j]['create_time']
                            log.info(mmcId + ' 的创建时间是：' + create_time)
                            return
                        elif (j + 1 == len(resp_dataList)):
                            log.warning('第'+ str(i) + '页未没有找到\n')


if __name__ == '__main__':
    unittest.main()