#!/usr/bin/env python

import shelve

f = shelve.open('shelve_test')


print(dir(f))

print(f)

b = f.get('t')

c = f.get("test")
print(c)