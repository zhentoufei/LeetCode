# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/5 21:00'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '39.二叉树的深度.py'

'''
利用递归实现。如果一棵树只有一个结点，那么它的深度为1。
递归的时候无需判断左右子树是否存在，因为如果该节点为叶节点，
它的左右子树不存在，那么在下一级递归的时候，直接return 0。
同时，记得每次递归返回值的时候，深度加一操作。
'''


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归方法求解，简单直接，时间复杂度O(n), 空间复杂度O(logn)
    def TreeDepth(self, p_root):
        if p_root == None:
            return 0
        else:
            return max(self.TreeDepth(p_root.left), self.TreeDepth(p_root.right)) + 1

    # 非递归算法，利用了一个栈和一个标志位栈
    def TteeDepth2(self, p_root):
        if not p_root:
            return 0

        depth = 0
        stack = []
        tag = []
        p_node = p_root
        while p_node or stack:
            while p_node:
                stack.append(p_node)
                tag.append(0)
                p_node = p_node.left

            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                p_node = None
            else:
                p_node = stack[-1]
                p_node = p_node.right
                tag.pop()
                tag.append(1) #添加1 代表了一种停止遍历的点
        return depth


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left =node7
    print Solution().TteeDepth2(node1)
