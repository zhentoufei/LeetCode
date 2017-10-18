# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/18 14:09'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '62.二叉树的序列化.py'

'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root):
        serialize_str = ''
        if root == None:
            return '#'

        stack = []
        while root or stack:
            while root:
                serialize_str += str(root.val) + ','
                stack.append(root)
                root = root.left
            serialize_str += '#,'
            root = stack.pop()
            root = root.right
        serialize_str = serialize_str[:-1] # 去掉最后的那个逗号
        return serialize_str

    def deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.deserialize_method(serialize, 0)
        return tree

    def deserialize_method(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize_method(s, sp)
        node.right, sp = self.deserialize_method(s, sp)
        return node, sp


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    print(Solution().serialize(node1))
