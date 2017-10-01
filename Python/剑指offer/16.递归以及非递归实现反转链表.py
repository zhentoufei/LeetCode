# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 10:05'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '16.递归以及非递归实现反转链表.py'


class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None

class Solution:

    def reverseList(self, p_head):
        p_reversed_head = None
        p_node = p_head
        p_prev = None

        while p_node != None:
            p_next = p_node.next

            if p_next == None: #遍历到最后一位
                p_reversed_head = p_node

            p_node.next = p_prev
            p_prev = p_node # 把指针p_prev指向当前的node
            p_node = p_next # 把指针p_node指向下一个node，以便下一次的运算
        return p_reversed_head

    def reverseListRec(self, p_head):
        if not p_head or not p_head.next:
            return p_head
        else:
            p_reversed_head = self.reverseListRec(p_head.next)
            p_head.next.next = p_head
            p_head.next = None
            return p_reversed_head


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    S = Solution()
    p = S.reverseListRec(node1)
    print(p.val)