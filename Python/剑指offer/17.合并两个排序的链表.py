# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 11:37'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '17.合并两个排序的链表.py'


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def merge(self, p_head_1, p_head_2):
        if p_head_1 == None:
            return p_head_2
        elif p_head_2 == None:
            return p_head_1

        p_merge_head = None
        if p_head_1.val < p_head_2.val:
            p_merge_head = p_head_1
            p_merge_head.next = self.merge(p_head_1.next, p_head_2)
        else:
            p_merge_head = p_head_2
            p_merge_head.next = self.merge(p_head_1, p_head_2.next)

        return p_merge_head


if __name__ == '__main__':
    pass
