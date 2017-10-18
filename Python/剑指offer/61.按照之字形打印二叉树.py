# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/17 11:14'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '61.按照之字形打印二叉树.py'


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, p_root):
        if not p_root:
            return []

        result = []
        nodes = [p_root]
        right = True
        while nodes:
            cur_stack = []
            next_stack = []
            if right:
                for node in nodes:
                    cur_stack.append(node.val)
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)
            else:
                for node in nodes:
                    cur_stack.append(node.val)
                    if node.left:
                        next_stack.append(node.right)
                    if node.right:
                        next_stack.append(node.left)

            next_stack.reverse()
            right = not right
            result.append(cur_stack)
            nodes = next_stack
        return result

    # 转换思路，存储的时候一直从左向右存储，打印的时候根据不同的层一次打印
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        levels, result, leftToRight = [root], [], True
        while levels:
            curValues, nextLevel = [], []
            for node in levels:
                curValues.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if not leftToRight:
                curValues.reverse()
            if curValues:
                result.append(curValues)
            levels = nextLevel
            leftToRight = not leftToRight
        return result


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

    S = Solution()
    aList = S.Print(pNode1)
    print(aList)
