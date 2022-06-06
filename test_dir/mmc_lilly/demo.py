#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/5/25 9:58 上午
# software: PyCharm
from test_dir.common.basic import timeToStamp

stime = '2022-06-01 14:21:11'
etime = '2022-06-06 15:57:43'

t1 = timeToStamp(stime)
t2 = timeToStamp(etime)

minutes = (t2 - t1 ) / 60

print(int(minutes / 0.5))