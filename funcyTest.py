#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funcy as _

a_list = [1, 2, 3, 4]

print "输出大于2的数字: ", _.filter(lambda num: num > 2, a_list)

print "所有数字+1 : ", _.map(lambda num: num + 1, a_list)

print "分组, 按照大于2, 小于2 进行分组: ", _.group_by(lambda num: num > 2 and "bigger" or "small", a_list)

a_dict = [{"num": 1, "gender": 1}, {"num": 2, "gender": 1}, {"num": 3, "gender": 2}, {"num": 4, "gender": 1}]

print "输出gender为1, num为偶数: ", _.filter(lambda obj: (obj["gender"] is 1 and obj["num"] % 2 == 0), a_dict)

print "提取a_dict中num", _.pluck("num", a_dict)

