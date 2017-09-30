# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/29 21:58'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '反向打印链表.py'

'''
面试题5：从头到尾打印链表：
从头到尾遍历链表，并用一个栈存储每个结点的值，
之后出栈输出值即可。
'''
class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, list_node):
        if list_node.val == None:
            return
        l=[]
        head = list_node
        while head:
            l.insert(0,head.val)
            head = head.next
        return l

if __name__ == '__main__':
    node1 = ListNode(10)
    node2 = ListNode(20)
    node3 = ListNode(30)
    node1.next = node2
    node2.next = node3

    singleNode = ListNode(12)

    s = Solution()

    print s.printListFromTailToHead(node1)