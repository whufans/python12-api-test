# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： logging j基础使用
"""
"""
1,定义一个日志收集器
2，设定级别 debug,info,error
3，设置日志格式
4，指定输出渠道
5，收集日志
6，关闭渠道
"""

import logging
from common import contants
# 定义一个日志收集器
my_logger = logging.getLogger('python12')
# 输出日志级别
my_logger.setLevel('DEBUG')
# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(lineno)s-%(message)s')
# 指定输出渠道
# 控制台输出
console = logging.StreamHandler()
console.setLevel('DEBUG')
console.setFormatter(formatter)

# 文件输出
file = logging.FileHandler(filename=contants.logs_file, encoding='utf-8')
file.setLevel('INFO')
file.setFormatter(formatter)

# error文件输出
error = logging.FileHandler(filename=contants.error_file, encoding='utf-8')
error.setLevel('ERROR')
error.setFormatter(formatter)


# 添加输出渠道到日志收集器里面
my_logger.addHandler(console)
my_logger.addHandler(file)
my_logger.addHandler(error)




if __name__ == '__main__':
    my_logger.debug('xiangziyou!!!!')
    my_logger.info('yuxuan!!!!')
    my_logger.error('33!!!!')


