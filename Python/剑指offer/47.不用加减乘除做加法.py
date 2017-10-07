# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/7 22:46'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '47.不用加减乘除做加法.py'

'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
扩展题目：
不使用新的变量，交换两个变量的值

方法一：基于加减法
a = a + b;  
b = a - b;  
a = a - b;  

方法二：基于异或运算
a = a ^ b;  
b = a ^ b;  
a = a ^ b;  

'''


# 利用异或以及与进位求解
# 不能一个正数一个负数
# 可能是python的的整型可以无限大的原因, 导致正数和负数的异或操作不断变成更小的负数而不会溢出
# 使用Swift尝试了一下, 还是可以求得正数和负数的位操作相加运算的
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry
        return num1



if __name__ == '__main__':
    s = Solution()
    print(s.Add(4, 2))
