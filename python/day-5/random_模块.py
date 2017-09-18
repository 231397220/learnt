#!/usr/bin/env python

import random

# print(random.randint(0,4))
#
checkcode = ''
for i in range(4):
    current = random.randint(0,4)
    if current != i:
        tmp = str(chr(random.randint(65,90)))
    else:
        tmp = str(random.randint(0,9))
    checkcode += tmp

print(checkcode)