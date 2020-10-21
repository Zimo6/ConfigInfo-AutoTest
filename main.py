import unittest
import time
from common import HTMLTestRunner


def get_test_cases(dir_path):
    # dir_path 是存放测试用例的文件路径
    test_cases = unittest.TestSuite()
    # 测试用例均使用"Test"开头命名
    suites = unittest.defaultTestLoader.discover(dir_path, 'Test*.py', top_level_dir=dir_path)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

"""
main 函数启动的话，配置文件路径为 “./”
TestCases 函数启动的话，配置文件路径为 “../”
"""
if __name__ == '__main__':
    cases = get_test_cases('./TestCase')
    now_time = time.strftime("%Y-%m-%d", time.localtime())
    filename = './report/' + now_time + '-report.html'  # 设置报告文件名
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'系统升级前后配置信息-自动化测试报告', description=u'详细测试结果如下:')
        runner.run(cases)
