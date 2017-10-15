# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/15 21:49'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '59.对称的二叉树.py'

'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, p_root):
        return

    def selfIsSymmetrical(self, p_root_1, p_root_2):
        if p_root_1 == None and p_root_2 == None:
            return True
        if p_root_1 == None or p_root_2 == None:
            return False
        if p_root_1.val != p_root_2.val:
            return False

        return self.selfIsSymmetrical(p_root_1.left, p_root_2.right) \
               and self.selfIsSymmetrical(p_root_1.right, p_root_2.left)


# 非递归实现判断二叉树是否对称
# 利用前序遍历

class Solution2:
    def isSymmetrical(self, p_root):
        pre_list = self.preOrder(p_root)
        mirror_pre_list = self.mirrorPreOrder(p_root)
        if pre_list == mirror_pre_list:
            return True
        return False

    def preOrder(self, p_root):
        if p_root == None:
            return [None]

        treeStack = []
        out_put = []
        p_node = p_root
        while p_node or len(treeStack) > 0:
            while p_node:
                treeStack.append(p_node)
                out_put.append(p_node.val)
                p_node = p_node.left
                if not p_node:
                    out_put.append(None)
            if len(treeStack):
                p_node = treeStack.pop()
                p_node = p_node.right
                if not p_node:
                    out_put.append(None)
        return out_put

    def mirrorPreOrder(self, p_root):
        if p_root == None:
            return [None]

        treeStack = []
        out_put = []
        p_node = p_root
        while p_node or len(treeStack) > 0:
            while p_node:
                treeStack.append(p_node)
                out_put.append(p_node.val)
                p_node = p_node.right
                if not p_node:
                    out_put.append(None)
            if len(treeStack):
                p_node = treeStack.pop()
                p_node = p_node.left
                if not p_node:
                    out_put.append(None)
        return out_put


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

    S = Solution2()
    result = S.isSymmetrical(pNode1)
    print(result)
