# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/24 21:29'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '矩形覆盖.py'

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

def solution_1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return solution_1(n-1)+solution_1(n-2)


if __name__ == '__main__':
    print solution_1(4)
