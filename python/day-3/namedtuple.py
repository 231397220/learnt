'''
可命名的元祖



'''

import collections
#创建类
MytupleClass = collections.namedtuple('MytupleClass',['x','y','z'])


t = MytupleClass(11,22,33)
print(t.x)
print(t.y)
# t[0]
# t.name
# t.age


