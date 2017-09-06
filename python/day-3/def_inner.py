'''
常用内置函数
abs() 绝对值
all()  所有元素为真,返回真
any()  只要有一个元素为真,返回真
ascii()   int.__repr__()
bin()     二进制,返回2进制值
bool()   判断真假
bytearray()  转换成字节     bytearray('张楠',encoding='utf-8')
bytes()      转换成字符串
callable()    是否可执行
chr(99) ord(c)   把数字转换成asc码   ,  把asc码转换成数字
delattr()      反射
dict()      dict(one=1, two=2)
dir()     当前变量所有的key
divmod()
enumerate()     for  i,item in enumerate(list,1):print(i,item)

eval()        eval("6*8")
map()         map(lambda x : x+100,list)
filter()    条件过滤
format()
frozenset()    不能增加修改的集合
globals()    当前可用的变量
hash()
hex()    16进制
max()     取列表中的最大值
min()      取列表中的最小值
oct()    8进制
open()    打开文件
range(N)    拿到0-N的区间
reversed()    反转
round()     四舍五入
sorted()   排序
sum()   求和
super()
vars()    当前变量所有的key和values


'''

print(all([1,2,3,4]))
print(all([]))

print(ascii(11))
print(int.__repr__(8))


f = lambda x:x+1
print(f(5))
print(callable(f))

def func(x):
    if x>33:
        return True
    else:
        return False

li = ['11','22','33','44']
print(filter(func,li))
