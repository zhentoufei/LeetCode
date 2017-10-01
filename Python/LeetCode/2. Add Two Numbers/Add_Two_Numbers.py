# -*- coding:utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
下面的解法来自：http://bookshadow.com/weblog/2015/04/05/leetcode-add-two-numbers/
def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def addTwoNumbers(self, l1, l2):
    head = ListNode(0)
    ptr = head
    carry  = 0
    while True:
        if l1 != None:
            carry += l1.val
            l1 = l1.next
        if l2 != None:
            carry += l2.val
            l2 = l2.next
        ptr.val = carry % 10
        carry /= 10
        # 运算未结束新建一个节点用于储存答案，否则退出循环
        if l1 != None or l2 != None or carry != 0:
            ptr.next = ListNode(0)
            ptr = ptr.next
        else:
            break
    return head
