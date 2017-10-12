# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/12 18:46'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '52.构建乘积数组.py'

'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


class Solution:
    def multiply(self, A):
        if A == None or len(A) <= 0:
            return

        lenght = len(A)
        a_list = [1] * lenght
        for i in range(1, lenght):
            a_list[i] = a_list[i - 1] * A[i - 1]

        tmp = 1
        for i in range(lenght - 2, -1, -1):
            tmp = tmp * A[i + 1]
            a_list[i] *= tmp

        return a_list


if __name__ == '__main__':
    pass
