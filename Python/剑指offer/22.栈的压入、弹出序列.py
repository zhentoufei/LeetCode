# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 14:25'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '22.栈的压入、弹出序列.py'

'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

class Solution:
    def isPopOrder(self, push_val, pop_val):
        if push_val == [] or pop_val == []:
            return False

        stack = []

        for i in push_val:
            stack.append(i)

            while stack != [] and stack[-1] == pop_val[0]:
                stack.pop()
                pop_val.pop(0)

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 3, 5, 2, 1]
    popVF = [4, 5, 2, 1, 3]
    S = Solution()
    print(S.isPopOrder(pushV, popV))