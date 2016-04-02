# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: generators
@create_time: 2016/4/2 14:14
"""
"""
生成器最佳应用场景：你不想将所有计算出来的大量结果集分配在内存当中，特别是结果集里包含大量循环，因为这样会造成大量的循环。
python2里的一些标准库函数会返回列表，而python3都修改成生成器，因为生成器更节省资源
在生成器对你有意义时候使用它，会非常有效
"""



def generator_function():
    for i in range(2):
        yield i

gen = generator_function()
print next(gen)
print next(gen)
# print next(gen)
# yield掉所有value时候，会触发stopIteration

for item in generator_function():
    print item
