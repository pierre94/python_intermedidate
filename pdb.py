# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: pdb
@create_time: 2016/4/2 14:14
"""
import pdb

def make_break():
    pdb.set_trace()
    return "I don't have time"

print (make_break())