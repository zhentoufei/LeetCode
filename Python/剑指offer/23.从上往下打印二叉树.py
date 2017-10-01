# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 15:11'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '23.从上往下打印二叉树.py'

'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。就是广度优先遍历
'''

'''
相当于按层遍历, 中间需要队列做转存
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def printFromTopToBottom(self, root):
        queue = []
        if not root:
            return []

        res = []
        queue.append(root)
        while len(queue)>0:
            cur_root = queue.pop(0)
            res.append(cur_root.val)
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        return res




if __name__ == '__main__':
    pass