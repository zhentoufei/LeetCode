# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/8 21:28'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '49.把字符串转换成整数.py'


class Solution:
    def strToInt(self, s):
        flag = False
        if s == None or len(s) < 1:
            return 0

        num_stack = []
        dic = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        for i in s:
            if i in dic.keys():
                num_stack.append(dic[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0

        ans = 0
        if len(num_stack) == 1 and num_stack[0] == 0:
            flag = True
            return 0
        for i in num_stack:
            ans = ans * 10 + i
        if s[0] == '-':
            ans = 0 - ans
        return ans


if __name__ == '__main__':
    test = '-123-56'
    s = Solution()
    print(s.strToInt(test))
