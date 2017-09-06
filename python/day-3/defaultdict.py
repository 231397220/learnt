#!/usr/bin/env python
'''
defaultdict    默认字典
将值的类型设置成list或其他.
在append时,可以直接使用.无需判断是否为第一个初始值,另做赋值.


'''


import collections

# dic = {'k1':[]}
# dic['k1'].append('sam')


dic = collections.defaultdict(list)
dic['k1'].append('sam')


print(dic)