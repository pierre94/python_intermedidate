# encoding: utf-8
"""
@author: pierre94
@contact: admin@bear2.cn
@site: pydocs.cn
@file: all_is_object
@create_time: 2016/4/2 15:16
"""
"""
主要讲解函数的对象性
第一个例子讲函数就是个对象
第二个讲函数中嵌套函数
第三个讲函数返回值是一个函数
"""

def hi(name='pierre'):
    return "hi "+name

print hi()

#此处没有小括号，因为不是在调用hi函数，而是将函数赋值给一个变量
greet = hi

print greet()

#删掉hi看看，hi不能运行了
del hi
#print hi()
# 但是greet还是可以运行
print greet()

################
# 函数中可以嵌套函数
def hello(name="pierre"):
    print "hello() function is ok~"

    def say_hello():
        return "say_hello() function is ok"

    def welcome():
        return "welcome function is ok"

    print say_hello()
    print welcome()

    print "you are back in the hello() function now "

hello()
# welcome()
# 在hello之外是不能调用welcome的

##########第三个例子
# 返回一个函数
def say_welcome(name="pierre"):
    def say_greet():
        return "greet "+name

    if name=="pierre":
        return say_greet
    else:
        return "hello"

a = say_welcome()
print a  #不执行
print a() #执行

#第四个例子
#将函数作为参数传给另外一个函数
def hi_hi():
    return "hi,hi!"

def doSomethingBeforeHi(func):
    print "I am doing something before function hi"
    print func()

doSomethingBeforeHi(hi_hi)