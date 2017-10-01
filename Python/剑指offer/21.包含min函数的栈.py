# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 14:15'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '21.包含min函数的栈.py'

'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)

        if self.min_stack == [] or node < self.min():
            self.min_stack.append(node)
        else:
            tmp = self.min()
            self.min_stack.append(tmp)

    def pop(self):
        if self.stack == [] or self.min_stack == []:
            return None
        self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return  self.stack[-1]

    def min(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    S = Solution()
    S.push(3)
    S.push(4)
    S.push(2)
    S.push(1)
    print(S.min())
    S.pop()
    print(S.min())
    S.pop()
    print(S.min())
