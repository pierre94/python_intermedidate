# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: set
@create_time: 2016/4/2 14:51
"""
"""
set 集合，与list相似，但是不能包含重复的值
set 可以比较方便的进行集合运算
"""
# 查找出list中重复的元素
one_list = ['a', 'b', 'a', 'c', 'd']

# for x in one_list :
#     if one_list.count(x)>1:
#         print x
        #找出重复的项目，一般会重复打印

# print set(one_list)  #去除list中重复的

duplicates = set([x for x in one_list if one_list.count(x)>1])
print duplicates

# 求交集
valid = set(['yello', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print input_set.intersection(valid)
# 求差集
print input_set.difference(valid)


