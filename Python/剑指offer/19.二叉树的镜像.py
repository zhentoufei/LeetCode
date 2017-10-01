# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 13:04'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '19.二叉树的镜像.py'


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归的方式实现
    def mirror(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return root

        p_tmp = root.left
        root.left = root.right
        root.right = p_tmp

        self.mirror(root.left)
        self.mirror(root.right)

    # 非递归的方式实现
    def mirror_2(self, root):
        if root == None:
            return
        stack_node = []
        stack_node.append(root)
        while len(stack_node) > 0:
            node_num = len(stack_node) - 1
            tree = stack_node[node_num]
            stack_node.pop()
            node_num -= 1

            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left

            if tree.left:
                stack_node.append(tree.left)
                node_num += 1

            if tree.right:
                stack_node.append(tree.right)
                node_num += 1

    # 非递归实现
    def mirror_3(self, root):
        if root == None:
            return

        node_queue = [root]
        while len(node_queue) > 0:
            cur_level = len(node_queue)
            count = 0
            while count < cur_level:
                count += 1
                p_root = node_queue.pop(0)
                root.left, root.right = root.right, root.left

                if root.left:
                    node_queue.append(root.left)
                if root.right:
                    node_queue.append(root.right)


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
    S.mirror_2(pNode1)
    print(pNode1.right.left.val)
