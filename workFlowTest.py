#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
流程控制
"""

if True:
    print "为true, 输出"

if False:
    print "false, 不输出"

# 遍历数组
a_list = [1, 2, 3, 4]
for i in a_list:
    print "遍历数组: ", i

# 遍历字典
a_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

for key in a_dict:
    print "遍历字典, key: %s, | value: %s" % (key, a_dict[key])

num = 0
while True:
    print "while循环中: ", num
    num += 1
    if num == 2:
        print "num等于2, 退出循环"
        break


# python中没有switch case, 使用dict进行模拟
def test1():
    return 1


def test2():
    return 2


a_dict = {1: test1, 2: test2}

param = 1
print "param为 %s, 调用相应映射函数, 结果: %s" % (param, a_dict[param]())
