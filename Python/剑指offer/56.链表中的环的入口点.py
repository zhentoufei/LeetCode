# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/14 9:53'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '56.链表中的环的入口点.py'


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None



class Solution:
    def meetingNode(self, p_head):
        if p_head == None:
            return None

        p_slow = p_head.next
        if p_slow == None:
            return None

        p_fast = p_slow.next
        while p_fast:
            if p_slow == p_fast:
                return p_slow

            p_slow = p_slow.next
            p_fast = p_fast.next

            if p_fast:
                p_fast = p_fast.next



if __name__ == '__main__':
    pass
