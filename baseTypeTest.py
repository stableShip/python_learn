# coding=utf-8

# 数字 int
num = 1
print(num)

# 数字 float
float1 = 0.1
float2 = 0.2
print(float1, float1 + float2)

# double精确度问题使用Decimal
import decimal

decimal.getcontext().prec = 1
float1 = decimal.Decimal(0.1)
float2 = decimal.Decimal(0.2)
print(float1, float(float2 + float1))

# string 中文必须在文件头声明# coding=utf-8
chinese = "中文"
print(chinese)

# string to number
a = "1"
print(int(a), type(int(a)))

# number to string
a = 1
print(str(a), type(str(a)))

# date
import datetime

today = datetime.date.today()
print("今天是 %s", today)

# boolean
is_true = True
is_false = False

# list 数组
a_list = [1, 2, 3, "list"]
print(type(a_list))

# tuple 元组
a_tuple = (1, 2, 3, "tuple")
print(type(a_tuple))

# dict 字典
a_map = {"name": "test"}
print(type(a_map))

# set
a_list = [1, 1, 2, 3, 4]
print(set(a_list), a_list, type(set(a_list)))
