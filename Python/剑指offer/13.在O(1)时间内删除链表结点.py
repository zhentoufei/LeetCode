# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 21:50'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '13.在O(1)时间内删除链表结点.py'

'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
当要删除的结点不是尾结点而且不是仅有一个结点的头结点，可以把该结点i的下一个结点j的内容复制到结点i，
同时把i结点的next指向j结点的next，然后再删除结点j。如果要删除的链表为单结点链表且待删除的结点就是头结点，
需要把头结点置为None，如果删除的结点为链表的尾结点，那么就需要顺序遍历链表，找到尾节点前面一个结点，
然后将其next置空。
'''


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def deleteNode(self, p_list_head, p_to_be_del):
        if not p_list_head or not p_to_be_del:
            return None

        if p_to_be_del.next != None:  # 使用下一个节点的值覆盖当前节点，删除下一个节点
            p_next = p_to_be_del.next
            p_to_be_del.val = p_next.val
            p_to_be_del.next = p_next.next
            p_next.__del__()
        elif p_list_head == p_to_be_del:  # 链表只有一个节点的时候，删除头结点（也是尾节点）
            p_to_be_del.__del__()
            p_to_be_del = None
            p_list_head = None
        else:  # 如果链表中有多个节点，删除尾部节点（也就是说，要删除的是最后一个节点）
            p_node = p_list_head
            while p_node.next != p_to_be_del:
                p_node = p_node.next

            p_node.next = None
            p_to_be_del.__del__()


if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node4 = ListNode(15)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    S = Solution()
    S.deleteNode(node1, node3)
    print(node3.val) # 打印出node4的结果
    S.deleteNode(node1, node3)
    print(node3.val) # 输出None
    print(node2.val)
    S.deleteNode(node1, node1)
    print(node1.val)
    S.deleteNode(node1, node1)
    print(node1.val)
