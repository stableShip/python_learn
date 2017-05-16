# coding=utf-8

# 读取文件方式一
a_file = open("./fileTest.py")
text = a_file.read()
# 显示调用close
a_file.close()
print ("文件类型: %s, 第一行内容: %s" % (type(text), text[0:15]))

# 读取文件方式二
with open('./fileTest.py', 'r') as f:
    print("第一行内容: %s" % f.readline())

# 写文件
with open('./test.txt', 'w') as f:
    f.write('Hello, world!')