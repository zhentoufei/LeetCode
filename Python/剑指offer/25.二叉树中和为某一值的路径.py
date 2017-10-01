# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 21:01'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '25.二叉树中和为某一值的路径.py'

'''
题目：输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径从树的根节点开始往下一直到
叶子节点所经过的节点所形成的一条路径
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, sum):
        if not root:
            return []

        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.pathSum(root.left, sum - root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.pathSum(root.right, sum - root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

    # 优化写法
    def pathSum(self, root, sum):

        if not root:
            return []

        if root.left == None and root.right == None:

            if sum == root.val:
                return [[root.val]]
            else:
                return []

        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]


if __name__ == '__main__':
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(5)
    pNode3 = TreeNode(12)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(7)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5

    S = Solution()
    print(S.FindPath(pNode1, 19))
