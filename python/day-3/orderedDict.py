#!/usr/bin/env python

'''
orderedDict   有序字典
方法 与字典一样
move_to_end('k1')  把指定KEY拿到最后
popitem()       默认拿最后一组的item
pop('k1')            默认拿最后一个key的值,拿指定key的值
update   增加数据

'''

import collections

dic = collections.OrderedDict()

dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'

print(dic)

dic.update({'k1':'v111','k5':'v555'})
print(dic)



# dic.move_to_end('k1')
# print(dic)

# ret = dic.popitem()
# print(dic)
# print(ret)

# ret = dic.pop('k2')
# print(dic)
# print(ret)