# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/6 20:49'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '41.和为s的两个数字.py'

'''
leetcode 的TwoSum问题啊
设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，对small和big求和，
如果和大于目标值，则从当前和中删除small值，并把small值加一，如果和小于目标值，则把big
值加一，再把新的big值加入和中。如果和等于目标值，就输出small到big的序列，同时把big加一
并加入和中，继续之前的操作。
'''
class Solution:
    def findNumsOfSum(self, arr, sum):
        if arr == None or len(arr) <= 0:
            return []
        if len(arr) >= 2 and sum > arr[-1] + arr[-2]:
            return []

        start = 0
        end = len(arr) - 1
        while start < end:
            tmp_sum = arr[start] + arr[end]

            if tmp_sum < sum:
                start += 1
            elif tmp_sum > sum:
                end -= 1
            else:
                return [arr[start], arr[end]]


if __name__ == '__main__':
    test = [1, 2, 4, 7, 11, 15]
    s = Solution()
    print(s.findNumsOfSum(test, 15))
