'''

对pickle数据 持久化



'''




import shelve

d = shelve.open('shelve_test')   #打开一个文件

class Test(object):
    def __init__(self,n):
        self.n = n


t = Test("This is T")
t2 = Test("this is T2")

name = ['sam',
        'timo',
        'jason']

d['test'] = name   #持久化列表
d['t'] = t         #持久化类
d['t2'] = t2

d.close()