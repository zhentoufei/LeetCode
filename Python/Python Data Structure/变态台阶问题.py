# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/24 21:03'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '变态台阶问题.py'


# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 这题是这组合数的和啊

def solution_1(n):
    return 2 ** (n - 1)


dict = {}


def solution_2(n):
    if n < 2:
        return 1
    else:
        return 2 * solution_2(n - 1)


if __name__ == '__main__':
    print solution_2(3)
