# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/8 21:37'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '50.二叉搜索树的最低公共祖先.py'


class TreeNode:
    def __init__(self,x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findParent(self, p_node_1, p_node_2, root):
        if p_node_1 == None or p_node_2 == None:
            return
        if p_node_2 == p_node_1:
            return

        val_1 = p_node_1.val
        val_2 = p_node_2.val

        while root != None:
            if (val_1-root.val)*(val_2-root.val) <= 0:
                return root.val
            elif val_1 > root.val and val_2 > root.val:
                root = root.right
            else:
                root = root.left

        return False

if __name__ == '__main__':
    pass