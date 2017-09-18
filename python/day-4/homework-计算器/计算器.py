#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re



'''

1-2*((60-30+(-40/5)*(9-2*5/-3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))


'''



# re.findall("")



def cale(formula):
    parentheses_flag = True
    while parentheses_flag:
        m = re.search("\([^()]+\)",formula)
        if m :
            print(m.group())
        break


pare = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

cale(pare)