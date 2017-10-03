# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/7 21:32'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'Triangle.py'


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        cur = triangle[0] + [float("inf")]
        for i in xrange(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in xrange(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [float("inf")]

        return reduce(min, cur)


if __name__ == "__main__":
    # print Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])

    print Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
