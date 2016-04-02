# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: map
@create_time: 2016/4/2 14:27
"""
"""
map会将一个函数映射到一个输出列表的所有元素上
"""

# 匿名函数配合map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print squared

# 一列表的函数。
def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print value