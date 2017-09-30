# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 9:53'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '用两个栈实现队列.py'

'''
面试题7：用两个栈实现队列：需要两个栈Stack1和Stack2，push的时候直接push进Stack1。
pop需要判断Stack1和Stack2中元素的情况，Stack1空的话，直接从Stack2 pop，Stack1不空的话，
把Stack1的元素push进入Stack2，然后pop Stack2的值。推广：用两个队列实现栈
'''


class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        if len(self.stack_2) == 0 and len(self.stack_1) == 0:
            return
        elif len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

if __name__ == '__main__':
    P = Solution()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())
