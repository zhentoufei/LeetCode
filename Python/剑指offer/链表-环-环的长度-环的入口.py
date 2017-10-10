# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/10 14:28'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '链表-环-环的长度-环的入口.py'


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:

    def isLoop(self, p_head):
        fast_node = p_head
        slow_node = p_head

        while slow_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            if fast_node == slow_node:
                break

        if fast_node == None or fast_node.next == None:
            return False
        else:
            return True


    def loopLength(self, p_node):
        if self.isLoop(p_node)== False:
            return 0
        fast_node = p_node
        slow_node = p_node
        length = 0
        begin = False
        again = False

        while fast_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            if fast_node == slow_node and again == True:
                break

            if fast_node == slow_node and again == False:
                begin = True
                again = True

            if begin == True:
                length += 1

        return length



    def findLoopEntrance(self, p_node):
        if self.isLoop(p_node) == False:
            return 0

        fast_node = p_node
        slow_node = p_node
        while fast_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            if fast_node == slow_node:
                break

        if fast_node == None or fast_node.next == None:
            return None

        slow_node = p_node
        while slow_node != fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next

        return slow_node






if __name__ == '__main__':
    pass