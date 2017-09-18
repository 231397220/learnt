#!/usr/bin/evn python

'''
创建列表
l1 = list(1,2,3,4,5,6)

l1 = [1,2,3,4,5]



列表方法

获取某个元素的索引  index
切片  obj[1:3]
向列表尾部添加一个元素,改变源列表    append
向指定位置下表添加一个元素   insert
删除  pop, del ,remove
删除并获取列表中最后一个元素,改变原列表    pop
指定删除值是什么的元素    remove
将列表翻转            reverse
长度  len
排序,改变源列表 sort
循环  for,while
循环终端     break:退出整个循环
            continue:退出当次循环
            pass:本次循环都不做,占位使用
            return:
            exit:退出程序
判断字符串是否在列表中,返回Trun和False     in      "alex" in ['shuaige'],
清空列表     clear
拷贝         copy
计算某个元素在列表里出现的次数    count
合并2个列表 或列表和元祖,改变原列表   extend






'''

li = ['aa','bb','cc','dd']
li.remove('aa')
print(li)


# li = [1,2,3,4,5]
# ret = li.pop()
# print(ret)


#
# t1 = (1,2,3,{'k1':'v1'})
#
# print(t1)
#
# t1[3]['k1'] = 'v2'
# print(t1)
#
#
#
# l1 = [11,22,33]    #list
#
#
# print(type(l1))
#

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

print list01
print list02

# 列表截取

print list01[0]
print list01[-1]
print list01[0:3]

# 列表重复

print list01 * 2

# 列表组合

print list01 + list02

# 获取列表长度

print len(list01)

# 删除列表元素

del list02[0]
print list02

# 元素是否存在于列表中

print 'john' in list02  # True

# 迭代

for i in list01:
    print i

# 比较两个列表的元素

print cmp(list01, list02)

# 列表最大/最小值

print max([0, 1, 2, 3, 4])
print min([0, 1])

# 将元组转换为列表

aTuple = (1,2,3,4)
list03 = list(aTuple)
print list03

# 在列表末尾添加新的元素

list03.append(5)
print list03

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

list03.extend(list01)
print list03

# 统计某个元素在列表中出现的次数

print list03.count(1)

# 从列表中找出某个值第一个匹配项的索引位置

print list03.index('john')

# 将对象插入列表

list03.insert(0, 'hello')
print list03

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

print list03.pop(0)
print list03

# 移除列表中某个值的第一个匹配项

list03.remove(1)
print list03

# 反向列表中元素

list03.reverse()
print list03

# 对原列表进行排序

list03.sort()
print list03