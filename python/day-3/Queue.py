#!/usr/bin/env python

'''
单向队列:一边放一边取. 先进先出

双向队列:二边放二边取

双向队列方法:
append      从右边添加
appendleft     从左边添加
count    计数,元素在队列里出现的次数
extend   扩展,多个元素添加
index    取 区间的值,默认从左取第一个.
insert   插入,任意位置
pop      取数据,右面去
rotate(N)   将最后N个元素放到第N个


单向队列方法
import queue
full  查看是否队列满
put   插入输入
get   取数据
qsize   查看有几个数据



'''

import collections
import queue

q = queue.Queue

d = collections.deque
d.
d.append('1')
d.appendleft('10')
d.appendleft('5')
print(d)