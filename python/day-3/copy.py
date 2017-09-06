#!/usr/bin/env python3


'''
深浅拷贝





'''


import copy



# #浅拷贝
# copy.copy()
#
# #深拷贝
# copy.deepcopy()
#
# #赋值
# a = 123


#字符串,数字

#列表,字典
# n1 = {'k1':'wu','k2':'123','k3':["sam",'678']}
#
# n2 = n1
#
# print(id(n1))
# print(id(n2))
#
# n3 = copy.copy(n1)
# print(id(n3))


dic = {
    'cpu':[80,],
    'mem':[80,],
    'disk':[80,]

}

new_dic = copy.copy(dic)
new_dic.['cpu'] = 50
print(new_dic)
