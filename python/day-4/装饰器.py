#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@login 就是装饰器, @login的意思是 代码 tv = login(tv). 所以@ 是一个语法糖,用来简化.

这个实验是有3个函数,客户都是直接调用的.但是后期需要在这些函数上,加上验证功能,希望验证后才可以使用此函数.
简单理解就是,希望在这3个函数中增加内容,但是遵从开放封闭原则.不能再源代码上进行修改.所以需要在原有函数的基础上在包一层新函数.
这样新函数和源函数将一起运行.
而客户的调用方法不变.

实现方法:
定义一个函数,但是在执行整个脚本时,由于@login的原因,会先执行此函数的内容.
会导致,执行脚本时.在没有调用函数时,先执行login中的内容.
解决方法是 在login函数中,创建一个内函数.在login函数中,return内涵数的
注意点:内函数中,不在需要return func的内存地址,而是直接执行func.
arg就是tv函数的内存地址.执行func(arg),就是执行tv('sam')函数.




'''

def login(func):
    def inner(arg):
        print("passed user verification......")
        func(arg)           #arg就是tv函数的内存地址.执行func(arg),就是执行tv('sam')函数.

 #   print("passed user verification......")
 #    return func
    return inner


def home(name):
    print("welcome [%s] to page" %(name))

@login
def tv(name):
    print("welcome [%s] to tv" %(name))


def moive(name):
    print("welcome [%s] to moive" %(name))


# tv = login(tv)
tv('sam')
# moive('sam')