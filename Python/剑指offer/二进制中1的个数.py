# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 15:54'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '二进制中1的个数.py'


# 1 & 1 = 1， 1 & 0 = 0 & 1 = 0 & 0 = 0
# 1 ^ 1 = 0 ^ 0 = 0， 1 ^ 0 = 0 ^ 1 = 1

# 数学方法
def numberOfOne(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        count += 1
        n = (n - 1) & n
    return count


# 自带函数方法
def numberOfOne2(n):
    count = 0
    if n < 0:
        s = bin(n & 0xffffffff)
    else:
        s = bin(n)
    return s.count('1')


# 判断一个数是不是2得整数次幂
def isPowerOfTwo(n):
    if n & (n - 1) == 0:
        return True
    else:
        return False


# 判断两个数的二进制表示有多少位不一样, 直接比较两个数的二进制异或就可以
def andOr(m, n):
    diff = m ^ n
    print diff
    count = 0
    while diff:
        count += 1
        diff = diff & (diff - 1)
    return count


if __name__ == '__main__':
    print andOr(2, 4)
