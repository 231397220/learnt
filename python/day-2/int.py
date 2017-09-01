#!/usr/bin/evn python

'''
int方法
bit_length   返回当前int使用的最少位数的二进制, 如1用1个,2用2个,3用2个.
__abs__      返回绝对值, age=-19 abs得19
__add__      相加  x.__add__(y)   ==  x+y
__and__      并且   a&b
__cmp__      比较   cmp(x,y)
__bool__
__divmod__   页面分页使用   (商,余数)
__eq__       判断是否相等  19 == 18
__float__    转换成float对象
__floordiv__   底板除   5.__floordiv__(6)  => 0   ==  5//6
__ge__       18.__ge__(99)   判断 18>=99
__pow__       幂 2**8 == 256


###实验操作
>>> divmod(95,10)
(9, 5)
>>> all=95
>>> one_piece=10
>>> divmod(all,one_piece)
(9, 5)

>>> a = 19
>>> a.__abs__()
19
>>> a=-19
>>> a.__abs__()
19
>>> help(abs)
>>> abs(-19)
19

>>> a.__add__(9)
-10
>>> a+9
-10

'''





age = 95


age = int(95)

float_result = age.__float__()
print(float_result)

print(age.__abs__())
print(abs(- 19))
print(age.bit_length())
print(type(age))

