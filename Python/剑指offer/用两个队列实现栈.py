# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 10:11'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '用两个队列实现栈.py'

class Solution:
    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x):
        if self.queue_2 == []:
            self.queue_1.append(x)
        else:
            self.queue_2.append(x)

    def pop(self):
        if not self.queue_1 and not self.queue_2:
            return
        if self.queue_1 != []:
            length = len(self.queue_1)
            for i in range(length-1):
                self.queue_2.append(self.queue_1.pop(0))
            return self.queue_1.pop()
        else:
            length = len(self.queue_2)
            for i in range(length-1):
                self.queue_1.append(self.queue_2.pop(0))
            return self.queue_2.pop()


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