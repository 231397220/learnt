#!/usr/bin/env python
# -*- coding:utf-8 -*-


def binary_search(date_source,find_num):
    mid = int(len(date_source)/2)
    # print(mid)
    # print(date_source[mid])
    if len(date_source) >= 1:
        if date_source[mid] > find_num:
            print("要找的数在左边,本轮判断数是%s" %date_source[mid])
            print(date_source[:mid])
            binary_search(date_source[:mid],find_num)
        elif date_source[mid] < find_num:
            print("要找的数在右边,本轮判断数是%s" %date_source[mid])
            print(date_source[mid:])
            binary_search(date_source[mid:],find_num)
        else:
            print("本轮判断数是%s" % date_source[mid])
            print("find it!!!")
    else:
        print("本轮判断数是%s" % date_source[mid])
        print("cannot find ....")



if __name__ == '__main__':
    data = list(range(1,60,3))
    binary_search(data, 1)
