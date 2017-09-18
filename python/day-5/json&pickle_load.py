#!/usr/bin/env python
'''

dump第一次是name  所以第一次load是name

需要按顺序load,所以建议使用shelve模块


'''

import pickle

f = open('pickle_test','rb')

a = pickle.load(f)

print(a)

b = pickle.load(f)

print(b)