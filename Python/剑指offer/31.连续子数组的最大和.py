# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 17:23'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '30.连续子数组的最大和.py'


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


if __name__ == '__main__':
    alist = [1, -2, 3, 10, -4, 7, 2, -5]
    s = Solution()
    print(s.FindGreatestSumOfSubArray2(alist))
