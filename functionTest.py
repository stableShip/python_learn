#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 基本定义
def test():
    return "test"


print "运行函数获取返回值: ", test()


# 函数参数默认值, 没有传相应参数, 使用默认值
def add(a, b=1):
    return a + b


print "函数默认值:", add(1), add(1, 2)


# 不定参数1
def read(*args):
    return args, type(args)


print "不定参数函数*args: ", read(1, 2, 3, 4)


# 不定参数2
def read2(**kwargs):
    return kwargs, type(kwargs)


print "不定参数函数**kwargs: ", read2(name=1, gender=2)
