# coding:utf-8

# 使用标准库operator下的methodcaller函数调用
from operator import methodcaller

s = 'asdsdfgf'
print s.find('sd', 0)

print methodcaller('find', 'sd', 0)(s)
