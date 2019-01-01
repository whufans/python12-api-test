# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

# 正则表达式完成字符串的查找
# s1 = 'world hello'
# pattern = 'hello'  # 正则表达式
# res = re.match(pattern=pattern, string=s1)  # 最开始位置查找,找到则返回一个match对象，无则返回None
# match3 = re.search(pattern=pattern, string=s1)  # 任意位置找，找到则返回一个match对象，无则返回None
# print(match3)
# res1 = re.findall(pattern=pattern, string=s1)  # 查找全部匹配字符串，并且将查找到的匹配字符放到一个列表里面
# print(res1)
# # 变量名#
s = '{"mobilephone":"${normal_user}","pwd":"${pwd}"}'

# # 目标字符串
# res4 = re.findall(pattern='(\d{11})',string=s)
#
# s1 = re.sub('\$\{(.*?)\}','123456',s)
# print(s1)
#
# res5 = re.search(pattern='\$\{(.*?)\}', string=s)
# print(res5.group(0), res5.group(1))
#
# # 正则表达式分组
# s4 = 'www.lemonban.com'
# p = '(w)(ww)' #  ()进行分组
# m = re.search(p,s4)
# print(m)
# print(m.group(0))  # 全匹配
# print(m.group(1))  # 拿到第一个分组里面的字符
# print(m.group(2))  # 拿到第二个分组里面的字符


import json
import re

# 使用字典解析 解析-遍历-判断-统计
with open('loads.txt', 'r', encoding='utf-8') as fp:  # 打开文件
    financelog = json.load(fp)  # 文件对象序列化成字典
    datas = financelog['data']  # 获取data列表
    flag = 0
    for data in datas: # 遍历列表
        if data['status'] == '1':  # 判断是否等于1
            flag += 1  # 统计status=1
    print("status=1 的条数为：", flag)

# 使用正则解析 匹配并查找
financelog = open('loads.txt', 'r', encoding='utf-8').read()  # 读取文件里面的内容并返回一个字符串
status = re.findall('"status": "1"', financelog)  # 匹配在目标字符串中查找"status": "1"的内容，放到一个列表里面
print("status=1 的条数为：", len(status))  # 获取列表的长度就代表有多少条"status": "1"的数据


#findall
s = '{"mobilephone":"${normal_user}","pwd":"${pwd}"}'
pattern = '\$\{(.*?)\}'
ss = re.findall(pattern,s)
print(ss)

re.sub(pattern,'aaa',s)
