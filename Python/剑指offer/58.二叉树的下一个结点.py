# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/10 14:28'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '链表-环-环的长度-环的入口.py'
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def getNext(self, p_node):
        if p_node == None:
            return
        p_next = None
        if p_node.right != None:
            p_right = p_node.right
            while p_right.left != None:
                p_right = p_right.left
            p_next = p_right
        elif p_node.next != None:
            p_cur = p_node
            p_parent = p_cur.next
            while p_parent != None and p_cur == p_parent.right:
                p_cur = p_parent
                p_parent = p_cur.next
            p_next = p_parent
        return p_next


if __name__ == '__main__':
    pass
