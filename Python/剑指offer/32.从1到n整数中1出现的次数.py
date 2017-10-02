# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 19:33'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '32.从1到n整数中1出现的次数.py'


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones

    def NumberOf1Between1AndN2(self, n):
        ones, m = 0, 1
        while m <= n:
            if ((n // m) % 10) != 0 and ((n // m) % 10) != 1:
                print 'a', ones
                ones += (n // 10 // m + 1) * m
            elif ((n // m) % 10) == 1:
                print 'b', ones
                ones += (n // m // 10) * m + n % m + 1
            m *= 10
        return ones


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(13))
    print(s.NumberOf1Between1AndN2(13))
