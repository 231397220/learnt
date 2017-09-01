
'''
字典方法
clear   清空所有元素
copy    浅拷贝
fromkeys    生成新字典
get         获取key对应的值,如果没有key返回none,或自定义参数    dic = {'k1':'v1','k2':'v2'}  print(dic.get('k3','sam'))
items       获取所有的键值对
keys        获取所有的keys
values      获取所有的values
pop         拿走指定key的value,修改源字典
popitme     随机拿走一组键值对
setdefault    dic['k'] = none
update      更新字典中增加或更新键值对的值.


'''











dic = {'k1':'v1','k2':'v2'}
dic.update({'k4':123})
dic.update({'k4':3})

print(dic)





# print(dic.popitem())
# print(dic)


#
#
# print(dic.items())
# print(dic.keys())
# print(dic.values())

# print(dic['k2'])
# print(dic.get('k3','sam'))
#
# new_dic = dic.fromkeys(['k1','k2'],'v1')
# print(new_dic)
