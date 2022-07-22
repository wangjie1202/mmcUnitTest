#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/4/22 4:08 下午
# software: PyCharm
"""
大app公共参数
"""
import warnings
import requests
from test_dir.common.basic import get_config
from test_dir.common.log import Log


class BigAppBasic():

    def __init__(self):
        self.warning = warnings.simplefilter("ignore", ResourceWarning)
        self.headers = {"Content-Type": "application/json"}
        self.se = requests.Session()
        self.host = get_config(name='bigAppHost', key='url')
        self.log = Log()



