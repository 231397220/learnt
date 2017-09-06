#!/usr/bin/env python

'''
add 添加
clear  清空
copy   浅拷贝
difference   差集,取不同,最后输出以源集合中元素,生成新的set,存储不同.
difference.update    改变源set,储存不同(不包含)元素,删除相同(包含)的元素
intersection  取交集,生成新的set
intersection.update   取交集,改变源set
isdisjoint          去过没有交集,返回true
issubset            判断是否是子集
issuperset         判断是否是父集
pop             取出一个元素,将次元素赋值给其他变量,随机
remove            删除指定元素
symmetric_difference  差集,对称差,最后输出为源集合和.创建新对象
symmetric_difference_update  差集,改变原来
union   并集
update  更新


'''



# s1 = set ()

# s2 = set(['alex','sam','timo','sam'])
#
# print(s2)
#
# # s3 = s2.difference(['sam','timo'])
# # print(s3)
#
# s2 = set(['alex','sam','timo','sam'])
#
# # s4 = s2.difference_update(['sam','timo'])
# # s3 = s2.pop()
# s3 = s2.remove('timo')
# print(s3)


old_dict = {
    "#1":{ 'hostname':"c1", 'cpu_count':2 ,'mem_capicity':80},
    "#2":{ 'hostname':"c1", 'cpu_count':2 ,'mem_capicity':80},
    "#3":{ 'hostname':"c1", 'cpu_count':2 ,'mem_capicity':80}
}


new_dict = {
    "#1":{ 'hostname':"c1", 'cpu_count':2 ,'mem_capicity':800},
    "#3":{ 'hostname':"c1", 'cpu_count':2 ,'mem_capicity':80},
    "#4":{ 'hostname':"c1", 'cpu_count':2 ,'mem_capicity':80}
}

old_dict.keys()
new_dict.keys()




# 交集:要更新的数据
# 老数据与更新数据的差集:要删除的数据
# 新数据与更新数据的差集:要增加的数据

old = set(old_dict.keys())
new = set(new_dict.keys())

print(old.difference(new))
print(old.symmetric_difference(new))

# update_set = old.intersection(new)
# delect_set = old.symmetric_difference(update_set)
#
# add_set= new.symmetric_difference(update_set)
#
# print(update_set,delect_set,add_set)
# print(old.symmetric_difference(update_set))
#
#

