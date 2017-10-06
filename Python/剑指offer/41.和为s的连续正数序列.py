# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/6 20:59'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '41.和为s的连续正数序列.py'

'''
题目：输入一个正数s，打印出所有和为s的连续正数序列（至少两个数字）
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15
所以输入的应该是[1,2,3,4,5], [4,5,6], [7,8]
'''


class Solution:
    def findNumListsOfSum(self, tar_sum):
        if tar_sum < 3:
            return []
        small = 1
        big = 2
        # mid = (tar_sum + 1) / 2
        mid = (tar_sum + 1) >> 1
        cur_sum = small + big
        res = []
        while small < mid:
            if cur_sum == tar_sum:
                res.append(list(range(small, big + 1)))
                big += 1
                cur_sum += big

            elif cur_sum < tar_sum:
                big += 1
                cur_sum += big
            else:
                cur_sum -= small
                small += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findNumListsOfSum(15))
