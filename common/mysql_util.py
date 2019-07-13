# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 数据库操作封装类
"""
"""
1,连接数据库
2, 编写一个sql
3, create cursor
4, execute  
"""

import pymysql

from common.config import ConfigLoader


class MysqlUtil:

    def __init__(self):
        config = ConfigLoader()
        host = config.get('mysql', 'host')
        port = config.getint('mysql', 'port')  # port 是一个数值
        user = config.get('mysql', 'usr')
        password = config.get('mysql', 'pwd')
        # 异常处理
        self.mysql = pymysql.connect(host=host, user=user, password=password,
                                     port=port, cursorclass=pymysql.cursors.DictCursor)

    def fetch_one(self, sql):  # 查询一条数据并返回
        cursor = self.mysql.cursor()
        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchone()  #

    def fetch_all(self, sql):  # 查询多条数据并返回
        cursor = self.mysql.cursor()

        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchall()  # ((),())

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    sql = 'select mobilephone from future.member where ' \
          ' mobilephone != ""  order by mobilephone desc limit 1 '
    print(sql)
    mysql_util = MysqlUtil()
    results = mysql_util.fetch_one(sql)
    # print(results[1])  # 不知道是哪一列
    print(results['mobilephone'])  # 根据字典的KEY进行取值
