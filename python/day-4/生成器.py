#!/usr/bin/env python
# -*- -*-
'''
报错函数的终端状态


'''

def cash_money(amount):
    while amount >0:
        amount -= 100
        yield 100
        print("又来取钱了!")


atm = cash_money(500)

print(type(atm))

print(atm.__next__())
print(atm.__next__())
print(atm.__next__())
print("买个大宝剑")
print(atm.__next__())
