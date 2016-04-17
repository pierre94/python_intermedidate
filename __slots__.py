# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: __slots__
@create_time: 2016/4/17 17:26
"""
class MyClass(object):
  __slots__ = ['name', 'identifier']
  def __init__(self, name, identifier):
      self.name = name
      self.identifier = identifier
      self.set_up()

