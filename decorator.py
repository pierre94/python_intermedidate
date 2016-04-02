# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: decorator
@create_time: 2016/4/2 15:50
"""
"""
装饰器decorator
封装一个函数，用修饰器改变它的行为
@wraps接受一个函数进行修饰，并加入复制函数名称、注释文档，参数列表等等功能，这样可以在修饰器里面访问在修饰之前的函数属性
装饰器常用场所：
授权、日志
"""
from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    print "Function is running"


can_run = True
print func()

can_run = False
print func()

#############
print "*"*20

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not auth or not check_auth():
            authenticate()
        return f(*args, **kwargs)
    return decorated

auth = True

def check_auth():
    pass

def authenticate():
    pass
