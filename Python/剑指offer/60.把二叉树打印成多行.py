# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/16 10:13'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '60.把二叉树打印成多行.py'

'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, p_root):
        if p_root == None:
            return []
        nodes, res = [p_root], []
        while nodes:
            cur_stack = []
            next_stack = []
            for node in nodes:
                cur_stack.append(node.val)
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            res.append(cur_stack)
            nodes = next_stack
        return res



if __name__ == '__main__':
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution()
    aList = S.Print(pNode1)
    print(aList)