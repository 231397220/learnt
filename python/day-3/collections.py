#!/usr/bin/env python

import collections

'''
collections 计算,继承dct所有方法,对字典的处理,计算元素出现的各种
Counter 将输入源,打碎成当个元素,并统计每个元素出现次数,输出字典.
most_common(5)   及counter后,取出最多出现次数前5名,输出列表.
elements         把每个元素,逐一打印出来
update           添加
subtract         删除     


'''

# obj = collections.Counter('adjfakldsajglda;jewq')
# print(obj)
#
# ret = obj.most_common(4)
# print(ret)
#
# for item in obj.elements():
#     print(item)

obj = collections.Counter(['11','22','33','55','11'])
print(obj)
# obj.update(['sam','22','22'])
# print(obj)
obj.subtract(['sam','22','22'])
print(obj)