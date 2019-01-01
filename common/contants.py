# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 常量管理 不会改变的变量
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径
# print(base_dir)

configs_dir = os.path.join(base_dir, 'configs')  # configs文件夹路径
# print(configs_dir)

datas_dir = os.path.join(base_dir, 'datas')  # datas文件夹路径
case_file = os.path.join(datas_dir, 'cases.xlsx')
# print(datas_dir)

reports_dir = os.path.join(base_dir, 'reports')  # reports文件夹路径
reports_html = os.path.join(reports_dir, 'reports.html')  # reports文件夹路径
# print(reports_dir)

logs_dir = os.path.join(base_dir, 'logs')  # logs文件夹路径
logs_file = os.path.join(logs_dir, 'logs.log')  # logs文件夹路径
error_file = os.path.join(logs_dir, 'error.log')  # logs文件夹路径
# print(logs_dir)

testcases_dir = os.path.join(base_dir, 'testcases')  # logs文件夹路径
