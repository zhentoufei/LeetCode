# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 12:45'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '18.树的子结构.py'

'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasSubTree(self, p_root_1, p_root_2):
        res = False
        if p_root_1 != None and p_root_2 != None:
            if p_root_1.val == p_root_2.val:
                res = self.doesTree1HasTree2(p_root_1, p_root_2)
            if not res:
                res = self.hasSubTree(p_root_1.left, p_root_2)
            if not res:
                res = self.hasSubTree(p_root_1.right, p_root_2)
        return res

    def doesTree1HasTree2(self, p_root_1, p_root_2):
        if p_root_2 == None:
            return True
        if p_root_1 == None:
            return False
        if p_root_1.val != p_root_2.val:
            return False

        return self.doesTree1HasTree2(p_root_1.left, p_root_2.left) \
               and self.doesTree1HasTree2(p_root_1.right, p_root_2.right)


if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print(S.hasSubTree(pRoot1, pRoot8))
