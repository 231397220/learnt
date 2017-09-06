#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

def consumer(name):
    print("%s is 吃包子" %name)
    while True:
        baozi = yield   #不是返回值,是接收值.

        print("包子[%s]来了,被[%s]吃了." %(baozi,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子了!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子")
        c.send(i)          #通过send方法,向C的consumer("A")的方法中yield传值.
        c2.send(i)

producer("sam")