#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'JIE'


class Test:
    # 构造函数
    def __init__(self):
        # 实例变量
        self.name = "name"

    # 类私有变量, 不可以在外部访问到
    __private_value = "private_value"

    # 类公开变量, 可以在外部访问到
    public_value = "public_value"

    # 实例私有方法(函数)
    def __test(self):
        print("private function")

    # 实例
    def public_func(self):
        print("public function")

    # 私有变量通过方法进行访问
    def get_private_value(self):
        return self.__private_value

    # 静态方法
    @staticmethod
    def static_test():
        return "static"

    # 类方法
    @classmethod
    def class_def_test(cls):
        return "classDefTest"

# 不可访问私有变量
try:
    Test.__private_value
except Exception, e:
    print "类私有变量应该不能打印, 报错: ", e

# 可访问公开变量
print "类公开变量:", Test.public_value

# 实例(对象)可以调用类方法, 类变量, 静态方法
print "实例调用类方法, 类变量, 静态方法: ", Test().public_value, Test().class_def_test(), Test().static_test()

try:
    # 类不能调用实例变量
    Test.name
except Exception, e:
    print "类不能调用实例变量: ", e

try:
    # 类不能调用实例方法
    Test.public_func()
except Exception, e:
    print "类不能调用实例方法: ", e

print "类能调用静态方法", Test.static_test()
