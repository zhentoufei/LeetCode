# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/5 20:21'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '37. 两个链表的第一个公共结点.py'

'''
方法1：利用堆栈的思想
首先，可以发现，如果过这两个链表有公共点，那么从公共节点到最后可定不会再分开了，
好了，我们就把这两个列表塞入堆栈中，然后分别pop出去
方法2：
就是下面的方法了，更加高效
[1]先比较出长短，找到之间的长度差
[2]让长的那个链表先走长度差这么多步数
[3]然后依次比较两个链表的节点
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findeFirstCommonNode(self, p_head_1, p_head_2):
        length_1 = self.getListLength(p_head_1)
        length_2 = self.getListLength(p_head_2)
        length_diff = abs(length_1-length_2)

        if length_1 > length_2:
            p_head_long = length_1
            p_head_short = length_2
        else:
            p_head_long = length_2
            p_head_short = length_1

        for i in range(length_diff):
            p_head_long = p_head_long.next

        while p_head_long != None and p_head_short != None and p_head_long != p_head_short:
            p_head_long = p_head_long.next
            p_head_short = p_head_short.next

        p_1st_common = p_head_long
        return p_1st_common

    def getListLength(self, p_head):
        length = 0
        while p_head != None:
            p_head = p_head.next
            length += 1
        return length


if __name__ == '__main__':
    pass