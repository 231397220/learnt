#!/usr/bin/env python



'''
递归算法是一种直接或间接的调用自身算法的过程.

1.递归就是在函数中调用自己
2.递归策略时,必须有明确的结束条件.
3.递归算法简洁,问题复杂时不建议使用递归方法.
4.递归调用过程中,容易造成内存溢出


要求
1.每一次调用,在上一次复杂度变小.
2.每次递归都是有条件的




'''


def calc(n):
    print(n)
    if n/2 > 1:
        ret = calc(n/2)
    print('返回时的n:%s' %n)
    return n


calc(10)


#斐波那契值

def func(arg1,arg2,stop):
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        func(arg2,arg3,stop)


func(0,1,30)