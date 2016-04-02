# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: decorator_logging
@create_time: 2016/4/2 16:36
"""
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__+" was called"
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    return x+x

result = addition_func(4)

# output:addition_func was called
