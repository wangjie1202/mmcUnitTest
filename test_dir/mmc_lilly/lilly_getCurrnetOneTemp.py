#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/5/24 10:06 上午
# software: PyCharm

"""
获取实时温度监控数据
"""
import unittest


from test_dir.common.basic import get_filePath, get_config, write_excelInfo, timeStampToStyleTime, update_excelInfo, \
    getUTCStamp, timeToStamp
from test_dir.common.log import Log
from test_dir.mmc_lilly.lilly_login import Login

log = Log()


class Send(unittest.TestCase):

    def setUp(self):
        self.url = get_config(name='lillyHost_online',key='url') + get_config(name='lilly_api',key='lilly_onetemp')
        self.getOrderInfo_url = get_config(name='lillyHost_online', key='url') + get_config(name='lilly_api', key='lilly_orderinfo')
        self.headers = Login().headers
        self.se = Login().se
        self.headers['Cookie'] = Login().get_userAuth()
        Login().warning

    def tearDown(self):
        log.info('---------- 测试结束 ----------\n')

    def test_getAllOneTemp(self):
        """
        获取某个运单所有实时温度数据
        :return:
        """
        log.info('---------- 测试开始 ----------')
        log.info('接口地址：' + self.getOrderInfo_url)
        gw_data = {
                    "gw_mac": "L201P85U00089",
                    "status": 1
        }
        log.info('请求参数：' + str(gw_data))
        gw_resp = self.se.post(url=self.getOrderInfo_url, headers=self.headers, json=gw_data)
        self.assertEqual(gw_resp.status_code, 200)
        self.assertEqual(gw_resp.json()['message'], 'get current info success')

        log.info("请输入要查询的秒秒测ID:")
        mmc_id = input()
        get_orderId = None
        get_Start_time = None
        gw_resp_data = gw_resp.json()['data']
        for i in range(0, len(gw_resp_data)):
            get_tagId = gw_resp_data[i]['tag_id']
            if (mmc_id==get_tagId):
                get_orderId = gw_resp_data[i]['orderid']
                get_Start_time = timeToStamp(gw_resp_data[i]['start_time'])
                break
            elif (i+1 == len(gw_resp_data)):
                log.error('未找到 ' + mmc_id)
                return False
        log.info(mmc_id + ' 查询指定温度标签成功')

        log.info('接口地址：' + self.url)
        currentTime = getUTCStamp()
        order_data = {
                        "start_time": get_Start_time,
                        "end_time": currentTime,
                        "order_id": get_orderId
        }
        log.info('请求参数：' + str(order_data))
        resp = self.se.post(url=self.url, json=order_data, headers=self.headers)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['message'], 'success')
        resp_data = resp.json()['data']
        tempExcel = get_filePath('test_data/mmc_lilly/'+mmc_id+'.xls')
        write_excelInfo(tempExcel, mmc_id, 0, 0, 'time')
        update_excelInfo(tempExcel, 0, 0, 1, 'temp')
        update_excelInfo(tempExcel, 0, 0, 2, 'rssi')
        log.info('正在下载数据，请稍后')

        # 获取时差（分钟数）公式：【(结束时间戳-开始时间戳)/60/60/24】该公式得到天数
        timeDiff = (currentTime - get_Start_time) /60
        log.info('记录时长（分钟）： ' + str(int(timeDiff)))
        log.info('应该上传点位：' + str(int(timeDiff / 2)))

        for i in range(0, len(resp_data)):
            # 写入时间
            utc8 = (int(resp_data[i]['scan_time'])+8*60*60)
            update_excelInfo(tempExcel, 0, i+1, 0, timeStampToStyleTime(utc8))
            # 写入温度
            update_excelInfo(tempExcel, 0, i+1, 1, resp_data[i]['temperature'])
            # 写入信号
            update_excelInfo(tempExcel, 0, i+1, 2, resp_data[i]['rssi'])
        log.info('写入完成')


if __name__ == '__main__':
    unittest.main()