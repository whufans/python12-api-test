# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import json
import unittest

from ddt import ddt, data

from common import contants
from common.do_excel import DoExcel
from common.request import Request
from common import logger1



@ddt
class TestLogin(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 实例化一个DoExcel对象
    cases = do_excel.get_cases('login')

    def setUp(self):
        print('测试准备')

    @data(*cases)
    def test_login(self, case):
        data = json.loads(case.data)
        logger1.my_logger.info('测试用例名称：{0}'.format(case.title))
        logger1.my_logger.info('测试用例数据：{0}'.format(case.data))
        resp = Request(method=case.method, url=case.url, data=data)  # 通过封装的Request类来完成接口的调用
        logger1.my_logger.debug('status_code:{0}'.format(resp.get_status_code()))  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        try:
            self.assertEqual(case.expected, resp.get_text())
        except AssertionError as e:
            logger1.my_logger.error('测试失败')

    def tearDown(self):
        print('测试清除')

