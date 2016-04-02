# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: decorator_logging_pro
@create_time: 2016/4/2 19:06
"""
"""
日志升级版本，可以实现不同函数生成不同调用日志。
此外可以写成装饰器类的形式
"""
from functools import wraps


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__+" was called"
            print log_string
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='out2.log')
def myfunc2():
    pass

myfunc2()