# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 22:23'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '14.调整数组顺序使奇数位于偶数前面.py'

'''
面试题14：
调整数组顺序使奇数位于偶数前面：注重函数的扩展性能。把函数中的判断条件写成一个判断条件的函数，方便与函数的扩展。
对于奇数位于偶数前面的情况，类似于快排，在头和尾分别设置一个指针，头指针指向奇数则后移，尾指针指向偶数则前移。
'''


# 方法1：采用和快速排序类似的思想来实现
def reOrderArr(arr):
    if len(arr) < 1:
        return
    elif len(arr) == 1:
        return arr

    front = 0
    rear = len(arr) - 1
    while front < rear: # 不可能出现front == rear的情况
        while arr[front] & 0x1 == 1:  # 奇数的时候
            front += 1
        while arr[rear] & 0x1 == 0:  # 偶数的时候
            rear -= 1

        if front < rear:
            arr[front], arr[rear] = arr[rear], arr[front]
    # arr[front], arr[rear] = arr[rear], arr[front]  # [1, 2, 3, 4, 5, 6, 7],在这种情况下会有多换一次的状况，我们需要
    return arr


# 方法2：使用python的推导表达式
def reOrderArr2(arr):
    if len(arr) < 1:
        return
    elif len(arr) == 1:
        return arr

    left = [x for x in arr if x & 1]
    right = [x for x in arr if not x & 1]
    return left + right


# 方法3：没意思
def reOrderArray3(self, array):
    if len(array) < 1:
        return []
    if len(array) == 1:
        return array
    arrayOdd = []
    arrayEven = []
    for num in array:
        if num & 0x1:
            arrayOdd.append(num)
        else:
            arrayEven.append(num)
    return arrayOdd + arrayEven


# 方法4：
def Reorder(pData, length, func):
    if length == 0:
        return

    pBegin = 0
    pEnd = length - 1

    while pBegin < pEnd:
        while pBegin < pEnd and not func(pData[pBegin]):
            pBegin += 1
        while pBegin < pEnd and func(pData[pEnd]):
            pEnd -= 1

        if pBegin < pEnd:
            pData[pBegin], pData[pEnd] = pData[pEnd], pData[pBegin]
    return pData


def isEven( n):
    return not n & 0x1


def isNegtive(n):
    return n >= 0


def ReorderOddEven(pData):
    length = len(pData)
    return Reorder(pData, length, func=isNegtive)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5, 6, 7]

    print reOrderArr(a)
    print reOrderArr(b)

    c = [1, 2, 3, 4, 5, 6]
    d = [1, 2, 3, 4, 5, 6, 7]
    print reOrderArr2(c)
    print reOrderArr2(d)

    e = [1, 2, 3, 4, 5, 6]
    f = [1, 2, 3, 4, 5, 6, 7]
    print ReorderOddEven(c)
    print ReorderOddEven(d)

    g = [1, 2, 3, 4, 5, 6]
    h = [1, 2, 3, 4, 5, 6, 7]
    print Reorder(g, len(g), isEven)
    print Reorder(h, len(h), isEven)
