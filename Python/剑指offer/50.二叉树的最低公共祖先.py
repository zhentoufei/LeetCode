# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/8 21:43'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '50.二叉树的最低公共祖先.py'


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p_node_1, p_node_2):
        if root == None:
            return False

        path_1 = self.storePath(root, p_node_1)[0]
        path_2 = self.storePath(root, p_node_2)[0]

        if path_1 and p_node_2:
            len_1 = len(path_1)
            len_2 = len(path_2)
            diff = abs(len_1 - len_2)
            if len_1 > len_2:
                mark_1 = len_1 - diff - 1
                mark_2 = len_2 - 1
            else:
                mark_1 = len_1
                mark_2 = len_2 - diff - 1

            while mark_1 >= 0 and mark_2 >= 0:
                if path_1[mark_1] == path_2[mark_2]:
                    return path_1[mark_1]
                mark_1 -= 1
                mark_2 -= 1

    def storePath(self, root, target_node):
        if root == None or target_node == None:
            return []

        elif root.val == target_node.val:
            return [[target_node.val]]

        stack = []
        if root.left:
            stack_left = self.storePath(root.left, target_node)
            for i in stack_left:
                i.insert(0, root.val)
                stack.append(i)

        if root.right:
            stack_right = self.storePath(root.right, target_node)
            for i in stack_right:
                i.insert(0, root.val)
                stack.append(i)

        return stack


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    res = []
    s = Solution()

    res = s.storePath(node1, node3)
    print res
