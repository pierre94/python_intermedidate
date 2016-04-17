# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: global
@create_time: 2016/4/17 16:13
"""
"""
global在这的意思是什么？global变量意味着我们可以在函数以外的区域都能访问这个变量。
在实际的编程时，你应该试着避开global关键字，它只会让生活变得艰难，因为它引入了多余的变量到全局作用域了。
"""

def add(value1, value2):
    global result
    result = value1+value2

# 测试global
add(1, 2)
print result

# 测试返回多个结果  profile_date是一个tup类型的
def profile():
    name = 'pierre'
    age = '22'
    return name, age

profile_date = profile()
print (profile_date)[1]