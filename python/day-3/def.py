#!/usr/bin/env/ python


'''
如果函数里没有return,返回值是None
return 不仅确认返回值,还退出程序.

参数
def mail(user):
   send user

mail(231397220@qq.com)



#默认参数 , 默认参数必须写在最后
def show(a1,a2=999):
    print(a1,a2)

show(111,22)


无参数
 show():   => show()

一个参数
def show(name):
    print(name)
show("sam")

二个参数

def show(name,age):
    print(name,age)
show("sam","18")


#指定参数
def show(a1,a2):
    print(a1,a2)

show(a2=1111,a1=99999)


#动态参数  --  元祖
def show(*arg):
    print(arg,type(arg))

show(1,'aa',4)


#动态参数  -- 字典
def show(**arg):
    print(arg,type(arg))

show(n1=22,n2=41,sam=[11,22])


#动态参数   ---   元祖+字典    元祖写在前面,字典写在后面
def show(*arg,**kwargs):
    print(arg,type(arg))
    print(kwargs,type(kwargs))

l= [11,22,33,44]
d = {'n1':22,'n2':"sam"}
show(l,d)
show(*l,**d)
show(11,22,33,44, n1=22,n2=2441)

'''

#指定参数
# def show(a1,a2):
#     print(a1,a2)
#
# show(a2=1111,a1=99999)

#默认参数
# def show(a1,a2=999):
#     print(a1,a2)
#
# show(111,22)
#
# def mail():
#     n = 123
#     n += 1
#     print(n)
#     return 'abc'
#
# mail()
# f = mail
# f()
#
# ret = mail()
# print(ret)
#
#
# def show():
#     print('a')
#     return [11,22]
#     print('b')
#
#
# ret = show()
# print(ret)

#动态参数  --  元祖
def show(*arg):
    print(arg,type(arg))

show(1,'aa',4)

#动态参数  -- 字典
def show(**arg):
    print(arg,type(arg))

show(n1=22,n2=41,sam=[11,22])

#动态参数   ---   元祖+字典
def show(*arg,**kwargs):
    print(arg,type(arg))
    print(kwargs,type(kwargs))

l= [11,22,33,44]
d = {'n1':22,'n2':"sam"}
show(l,d)
show(*l,**d)
show(11,22,33,44, n1=22,n2=2441)


s1 = '{0} is {1}'
#ret = s1.format('sam','man')
l = ['sam','man']

ret = s1.format(*l)

print(ret)