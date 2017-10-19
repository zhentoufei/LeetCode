# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/18 15:59'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '63.二叉搜索树的第k个节点.py'

'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.treeNode = []

    def inOrder(self, p_root):
        if len(self.treeNode) < 0:
            return None
        if p_root.left:
            self.inOrder(p_root.left)
        self.treeNode.append(p_root)
        if p_root.right:
            self.inOrder(p_root.rigth)

    def kthOrder(self, p_root, k):
        if k == 0 or p_root == None:
            return
        self.inOrder(p_root)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k - 1]

    def kthNode2(self, p_root, k):
        if k <= 0 or not p_root:
            return None
        tree_stack, nodes_que = [], []
        p_node = p_root
        while p_node or len(tree_stack):
            while p_node:
                tree_stack.append(p_node)
                p_node = p_node.left
            if len(tree_stack):
                p_node = tree_stack.pop()
                nodes_que.append(p_node)
                p_node = p_node.right
        if k > len(nodes_que):
            return None
        return nodes_que[k - 1]


if __name__ == '__main__':
    pass
