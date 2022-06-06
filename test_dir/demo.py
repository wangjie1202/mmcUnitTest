#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangjie
# datetime: 2022/1/13 3:13 下午
# software: PyCharm

from test_dir.common.basic import list_outputExcelInfo, get_filePath, update_excelInfo, read_excelInfo

write_filepath = get_filePath("test_data/result.xls")
read_filepath = get_filePath("test_data/demotest.xls")
#读取excel输出成数组
arr = list_outputExcelInfo(read_filepath, 0,1,1)
#读取数组内的基数下标
arr = arr[::2]
count = 0
for i in range(0, len(arr)):
    if arr[i] == 30:
        num1 = arr[i] * 3
        count+=1
        #读取参与计算数值同一行下一列的值
        value = read_excelInfo(read_filepath, 0).cell(i, 2).value
        #更新写入计算后的值、读取到的值
        update_excelInfo(write_filepath, 0, count, 1, num1)
        update_excelInfo(write_filepath, 0, count, 2, value)
    if arr[i] == 40:
        num2 = arr[i] * 4
        count+=1
        value = read_excelInfo(read_filepath, 0).cell(i, 2).value
        update_excelInfo(write_filepath, 0, count, 1, num2)
        update_excelInfo(write_filepath, 0, count, 2, value)
