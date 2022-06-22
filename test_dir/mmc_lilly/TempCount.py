#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/5/25 9:58 上午
# software: PyCharm
from test_dir.common.basic import timeToStamp


stime = '2022-06-10 18:58:00'
etime = '2022-06-11 00:00:00'
interval = 1

t1 = timeToStamp(stime)
t2 = timeToStamp(etime)

minutes = (t2 - t1) / 60
print("时长（分钟）：", minutes)
print("温度点位：", int(minutes / interval))