# -*- coding:utf-8 _*-
""" 
@author:mongo
@file: request.py 
@version:
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import json

import requests

from common.config import ConfigLoader


class Request:
    """
        Requests 封装类
        实现只需调用一个方法，来支持完成多种请求方式（get,post,delete....）的请求
        """

    def __init__(self, method, url, data=None, cookies=None, headers=None):
        try:
            config = ConfigLoader()
            url_pre = config.get('api', 'url_pre')
            url = url_pre + url  # 拼接请求地址
            if method == 'get':
                self.resp = requests.get(url=url, params=data, cookies=cookies, headers=headers)
            elif method == 'post':
                self.resp = requests.post(url=url, data=data, cookies=cookies, headers=headers)
            elif method == 'delete':
                self.resp = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):  # 返回响应码
        return self.resp.status_code

    def get_text(self):  # 返回str类型的响应体
        return self.resp.text

    def get_json(self):  # 返回dict类型的响应体
        json_dict = self.resp.json()
        # 通过json.dumps函数将字典转换成格式化后的字符串
        resp_text = json.dumps(json_dict, ensure_ascii=False, indent=4)
        print('response: ', resp_text)  # 打印响应
        return json_dict

    def get_cookies(self, key=None):  # 返回cookies
        if key is not None:
            return self.resp.cookies[key]
        else:
            return self.resp.cookies
