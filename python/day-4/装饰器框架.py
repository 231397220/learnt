#!/usr/bin/env python
# -*- coding:utf-8 -*-


def Before():
    print("Before")

def After():
    print("After")


def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            before_func(request,kargs)

            main_func(request,kargs)

            after_func(request,kargs)

        return wrapper

    return outer


@Filter(before,after)
def show():
    print('This is show func')

show()