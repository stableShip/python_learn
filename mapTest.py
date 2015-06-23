# coding=utf-8
__author__ = 'JIE'

list = [1, 2, 3, 4, 5]

print map(lambda x, y: x + y, list, list)

print map(lambda x: str(x + 1), list)

print map(str, list)


