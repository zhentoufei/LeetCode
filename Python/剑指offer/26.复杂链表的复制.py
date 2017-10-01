# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 22:15'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '26.复杂链表的复制.py'

'''
题目：实现一个复制复杂链表的函数。在复杂链表中，每个节点除了有一个m_pNext指针指向下一个节点外，
还有一个m_pSibling指向链表中的任意节点或者NULL
'''
'''
注意链表结点进行复制的时候，不能简单地写作 pCloned = pNode，这样的话之后对pCloned的操作也会作用在pNode上面，导致操作循环往复。
需要重新定一个pCloned = ListNode(0)，然后对结点的.val .next .random 进行设置。
同时，在将复制的结点的random指向原始链表结点的random的next的时候，需要先判断一下，原始链表结点的next是否为None，不为None再指向。
'''


class RandomListNode:
    def __init__(self, x=None):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def clone(self, p_head):
        if p_head == None:
            return None

        self.cloneNodes(p_head)
        self.connectRandomNodes(p_head)
        return self.reConnectNodes(p_head)

    # 先来复制原始链表的每个节点，将复制的节点连接在其原始节点的后面
    def cloneNodes(self, p_head):
        p_node = p_head
        while p_node:
            p_clone = RandomListNode(0)
            p_clone.label = p_node.label
            p_clone.next = p_node.next

            p_node.next = p_clone
            p_node = p_clone.next

    # 将复制后的链表中的复制节点的random指针连接到被复制的节点random指针的后一个节点
    def connectRandomNodes(self, p_head):
        p_node = p_head
        while p_node:
            p_clone = p_node.next
            if p_node.random != None:
                p_clone.random = p_node.random.next
            p_node = p_clone.next

    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def reConnectNodes(self, p_head):
        p_node = p_head
        p_cloned_head = None
        p_cloned_node = None
        if p_node != None:
            p_cloned_head = p_cloned_node = p_node.next
            p_node.next = p_cloned_head.next
            p_node = p_node.next

        while p_node:
            p_cloned_node.next = p_node.next
            p_cloned_node = p_cloned_node.next
            p_node.next = p_cloned_node.next
            p_node = p_node.next

        return p_cloned_head


if __name__ == '__main__':
    node1 = RandomListNode(1)
    node2 = RandomListNode(3)
    node3 = RandomListNode(5)
    node1.next = node2
    node2.next = node3
    node1.random = node3

    S = Solution()
    clonedNode = S.clone(node1)
    print(clonedNode.random.label)
