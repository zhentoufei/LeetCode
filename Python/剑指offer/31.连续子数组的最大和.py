# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 17:23'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '30.连续子数组的最大和.py'

import sys


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0

        nCurSum = 0
        nGreatestSum = array[0]
        for i in range(len(array)):
            if nCurSum <= 0:
                nCurSum = array[i]
            else:
                nCurSum += array[i]

            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum

        return nGreatestSum

    def FindGreatestAvgfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0

        nCurSum = 0
        nGreatestSum = array[0]
        for i in range(len(array)):
            if nCurSum <= 0:
                nCurSum = array[i]
            else:
                nCurSum += array[i]

            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum

        return nGreatestSum


        # 动态规划解决问题

    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array) <= 0:
            return 0
        aList = [0] * len(array)
        for i in range(len(array)):
            if i == 0 or aList[i - 1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = aList[i - 1] + array[i]
        return max(aList)


def FindGreatestAvgfSubArray(length, array, k):
    if array == None or length <= 0 or k <= 0:
        return 0

    if k > length:
        return 0

    nCurSum = sum(array[0:k])
    nGreatestSum = nCurSum
    for i in range(len(array)):
        if i < length - k:
            nCurSum -= array[i]
            nCurSum += array[i + k]
            if nCurSum < nGreatestSum:
                continue
            else:
                nGreatestSum = nCurSum

    return nGreatestSum / float(k)


if __name__ == '__main__':
    length = sys.stdin.readline().strip()
    a_list = sys.stdin.readline().strip().split(',')
    input_list = []
    for i in a_list:
        input_list.append(int(i))

    k = int(sys.stdin.readline().strip())
    print FindGreatestAvgfSubArray(length, input_list, k)
