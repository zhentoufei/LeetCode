# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 9:56'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '15.链表中倒数第k个结点.py'

'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def findKthToTail(self, head, kth):
        if head == None or kth <= 0:
            return None

        p_a_head = head
        p_b_behind = None

        for i in range(kth-1):
            if p_a_head.next != None:
                p_a_head = p_a_head.next
            else:
                return None

        p_b_behind = head
        while p_a_head.next != None:
            p_a_head = p_a_head.next
            p_b_behind = p_b_behind.next

        return p_b_behind



if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    S = Solution()
    print(S.findKthToTail(node1, 1).val)