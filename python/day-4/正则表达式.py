#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re




m = re.match('[0-9]','6ab1cdef')  #匹配所有数字,match方法从开头匹配

m = re.match('[0-9]{0,10}','6432151ab1cdef')    # {0,10}匹配0到10次,或者直接写{10},只匹配10次
if m:
    print(m.group())

m = re.findall('[0-9]{1,10}','6432151ab1cd2ef')   #把所有的数字匹配出来
m = re.findall('[a-zA-Z]{1,10}','6432151ab1cd2ef')    #把所有的字母取出来

m = re.findall('.*','6432 151ab1cd2ef')            #匹配任意字符

m = re.findall('.','6432 151ab1cd2ef')         #匹配一个

m = re.findall('.+','6432 151ab1cd2ef')        #匹配多个

m = re.findall('\S','64@32 151.ab1_cd2ef')         #匹配所有字符

m = re.findall('[a-zA-Z]+','64@32 151.ab1_cd2def')      #匹配多个字母

m = re.search('\d+','a64@32 151.ab1_cd2def')          #找到第一个数字


m = re.sub('\d+','|','a64@32 151.ab1_cd2def')         #把所有数字替换成 |

m = re.sub('\d+','|','a64@32 151.ab1_cd2def',count=2)    #只替换前2个数字,替换成 |

m = re.search('^\d+','5a64@32 151.ab1_cd2def')    #开头查找数字

m = re.search('^\d+$','13810606088')



if m:
    print(m)