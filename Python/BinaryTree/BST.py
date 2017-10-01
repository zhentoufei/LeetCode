# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/25 12:15'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'BST.py'


class Node(object):
    def __init__(self, ele=-1, lchild=None, rchild=None):
        self.ele = ele
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, ele):

        node = Node(ele)
        if self.root.ele == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    def front(self, root):
        if root == None:
            return
        print root.ele
        self.front(root.lchild)
        self.front(root.rchild)

    def middle(self, root):
        if root == None:
            return
        self.middle(root.lchild)
        print root.ele
        self.middle(root.rchild)

    def later(self, root):
        if root == None:
            return
        self.later(root.lchild)
        self.later(root.rchild)
        print root.ele



if __name__ == '__main__':
    eles = range(10)
    print eles
    tree =  Tree()
    for ele in eles:
        tree.add(ele)

    print '\n\n递归实现先序遍历'
    tree.front(tree.root)
