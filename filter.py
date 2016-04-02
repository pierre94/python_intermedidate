# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: filter
@create_time: 2016/4/2 14:46
"""
"""
filter 建一个表，其中每个元素都是对一个函数能返回一个true
filter 类似一个for循环，而且是一个内置函数，速度更快
"""

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x<0, number_list))
print less_than_zero