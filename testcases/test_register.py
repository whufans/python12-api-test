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
from common.mysql_util import MysqlUtil
from common.request import Request
from common.logger2 import MyLog


do_excel = DoExcel(contants.case_file)
cases = do_excel.get_cases('register')


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = MysqlUtil()
        sql = 'select mobilephone from future.member where ' \
              ' mobilephone != ""  order by mobilephone desc limit 1 '

        global max_phone
        max_phone = mysql.fetch_one(sql)['mobilephone']

    # def setUp(self):
    #     # 查询最大手机号码
    #     self.mysql = MysqlUtil() #
    #     self.sql = 'select mobilephone from future.member where ' \
    #                ' mobilephone != ""  order by mobilephone desc limit 1 '
    #
    #     self.max_phone = self.mysql.fetch_one(self.sql)['mobilephone']

    @data(*cases)
    def test_register(self, case):
        data = json.loads(case.data) # 将字符串序列化为字典
        if data['mobilephone'] == '${register}':  # 判断是否是需要进行参数化
            data['mobilephone'] = int(max_phone) + 1  # 取到数据库里面最大的手机号码进行加1
        MyLog.info('测试用例名称：{0}'.format(case.title))
        MyLog.info('测试用例数据：{0}'.format(case.data))
        MyLog.error('测试用例数据error')
        resp = Request(method=case.method, url=case.url, data=data)  # 通过封装的Request类来完成接口的调用
        MyLog.debug('status_code:{0}'.format(resp.get_status_code()))
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected, resp.get_text())
        if resp_dict['code'] == 20110: # 注册成功的数据校验，判断数据库有这条数据
            sql = 'select * from future.member where mobilephone = "{0}"'.format(max_phone)
            expected = int(self.max_phone) + 1
            member = self.mysql.fetch_one(sql)
            if member is not None: # 正常注册成功就不应该返回None
                self.assertEqual(expected,member['mobilephone'])
            else:# 返回None则代表注册成功之后但是数据库里面没有插入数据
                MyLog.error('注册失败')
                raise AssertionError

        # else：#  注册失败的数据校验，判断数据库没有这条数据，自己写

    # def tearDown(self):
    #         self.mysql.close()


    @classmethod
    def tearDownClass(cls):
        mysql.close()
