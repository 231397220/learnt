#!/usr/bin/evn python

'''
字符串 方法


移除空格 strip
分割并转换成列表 split
确认字符串里有多少个远程,长度  len(obj)
索引  obj[1]
切片  obj[1:2] ,

判断是否包含    __contains__     name.__contains__('sa')   ==> 'sa' in name
判断是否相等    __eq__
字符串的格式化   __format__    ???
反射的时候会使用    __getattribute__
__getitem__

首字母大写                    capitalize
居中显示                     center         name.center(22,"=")
计算a出现的次数               count      name.count(a)
计算s在前6位出现的次数         count   name.count("s",0,6)
编码 UTF8 转码 gbk          encode      name.encode('gbk')
判断字符串以什么字符结尾的     endswith    name.endswith('m',0,3)
判断字符串以什么开头    startswith
转换,将tab转换成8个空格       expandtabs
查找,查找元素在字符串中第几个位置,从0开始.查找不到时返回-1  find
查找,查找元素在字符串中第几个位置,从0开始.查找不到时报错  index
字符串格式化,字符串拼接和替换      format   name = "sam is a man {name} {1}"    name.format(name='cool','tow')
判断是数字    isalnum
判断是否是字母   isalpha
判断是否是十进制小数  isdecimal
判断是否是数字   isdigit
判断是否全是小写    islower
判断是否是全部大写   isupper
将列表转换成字符串,可自定义元素之间拼接付   join    "_".join(li)
将字符串放到最左边    ljust   rjust
变成小写                lower
将最左边的空格去掉       lstrip   rstrip
将字符串分割成    partition
将字符串中的摸个元素替换,可指定替换数量   replace
根据换行符进行切割,转换成列表      splitlines
将字符串中所有元素大小写互相转换      swapcase
将所有单词首字母大写     title
大写  upper
zfill



'''


name = ' s am isman '

print(name.strip())
print(name.__len__())
print(name.split('a'))

print(name.replace("s",'o',1))
print(type(name.partition("is")))

# li = ['s','b','a','l','e','x',]
# result = "_".join(li)
# print(result)


#
# name = "sam is a man {0} {1}"    #str __init__ 方法
#
# print(name.format('cool','tow'))
#
# print(name.find('is'))
#
# print(name.endswith('m',0,3))
#
# print(name.count("s",0,6))
#
# print(name.capitalize())
# print(name.center(22,"="))
#
# result =  name.__contains__('sa3')
# print(result)

#
#
# print(type(name))   #获取类
# print(dir(name))    #获取类中的成员(方法)
#
# tap_name = "sam\tis\ta"
# print(tap_name.expandtabs(10))