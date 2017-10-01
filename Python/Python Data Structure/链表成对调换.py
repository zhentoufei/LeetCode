# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/24 22:02'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '链表成对调换.py'

# 1->2->3->4转换成2->1->4->3.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def swapPairs(self, head):
        if head!=None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head

if __name__ == '__main__':
    pass
