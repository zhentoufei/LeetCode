# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/29 22:07'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '重建二叉树.py'

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def reConstructBTWithPreTin(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None

        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBTWithPreTin(pre[1:i + 1], tin[:i])
        root.right = self.reConstructBTWithPreTin(pre[i + 1:], tin[i + 1:])
        return root

    def reConstructBTWithTinLat(self, tin, lat):
        if not tin and not lat:
            return None
        if set(tin) != set(lat):
            return None

        root = TreeNode(lat[-1])
        i = tin.index(lat[-1])

        root.left = self.reConstructBTWithTinLat(tin[:i], lat[:i])
        root.right = self.reConstructBTWithTinLat(tin[i + 1:], lat[i:-1])
        return root

    def front(self, root):
        if root == None:
            return
        print root.val
        self.front(root.left)
        self.front(root.right)

    def middle(self, root):
        if root == None:
            return

        self.middle(root.left)
        print root.val
        self.middle(root.right)

    def later(self, root):
        if root == None:
            return

        self.later(root.left)
        self.later(root.right)
        print root.val


if __name__ == '__main__':
    # pre = [1, 2, 3, 5, 6, 4]
    # tin = [5, 3, 6, 2, 4, 1]
    pre = [1, 2, 4, 5, 7, 8, 3, 6]
    tin = [4, 2, 7, 5, 8, 1, 3, 6]
    lat = [4, 7, 8, 5, 2, 6, 3, 1]
    test = Solution()
    newTree = test.reConstructBTWithPreTin(pre, tin)
    newTree1 = test.reConstructBTWithTinLat(tin, lat)
    test.front(newTree1)
