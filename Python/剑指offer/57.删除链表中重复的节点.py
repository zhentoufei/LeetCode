# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/14 20:59'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '57.删除链表中重复的节点.py'

class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, p_head):
        if p_head == None:
            return
        pre_head = None
        p_node = p_head
        while p_node != None:
            need_del = False
            next_node = p_node.next
            if next_node != None and next_node.val == p_node.val:
                need_del = True
            if need_del == False:
                pre_head = p_node
                p_node = p_node.next
            else:
                node_val = p_node.val
                p_to_be_del = p_node
                while p_to_be_del != None and p_to_be_del.val == node_val:
                    p_to_be_del = p_to_be_del.next
                if pre_head == None:
                    p_head = p_to_be_del
                    p_node = p_to_be_del
                    continue
                else:
                    pre_head.next = p_to_be_del
                p_node = pre_head
        return p_head

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    s = Solution()
    print(s.deleteDuplication(node1).next.next.val)