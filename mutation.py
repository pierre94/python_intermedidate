# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: mutation
@create_time: 2016/4/17 17:13
"""
"""
对象变动(Mutation)
Python中可变(mutable)与不可变(immutable)的数据类型让新手很是头痛。
简单的说，可变(mutable)意味着"可以被改动"，而不可变(immutable)的意思是“常量(constant)”
"""



def add_to_immutable(num, target = None):
    if target is None:
        target = []
    target.append(num)
    return target

print add_to_immutable(1)

print add_to_immutable(2)


def add_to_mutable(num, target = []):
    target.append(num)
    return target

print add_to_mutable(1)
print add_to_mutable(2)

