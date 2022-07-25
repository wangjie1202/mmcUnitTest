# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
from BeautifulReport import BeautifulReport
from test_dir.common.basic import get_filePath, getNowTime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    test_suite = unittest.defaultTestLoader.discover("test_dir/mmc_bigapp", pattern="test_BigApp_login.py")
    result = BeautifulReport(test_suite)
    result.report(filename='秒秒测大App登录接口测试_' + getNowTime(), description='秒秒测大App_登录接口测试', report_dir=get_filePath("reports"))

    # test_suite = unittest.defaultTestLoader.discover("test_dir/mmc_bigapp", pattern="test_*.py")
    # result = BeautifulReport(test_suite)
    # result.report(filename='秒秒测大App测试报告_' + getNowTime(), description='秒秒测大App测试报告', report_dir=get_filePath("reports"))
