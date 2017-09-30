# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 20:39'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '打印1到最大的n位数.py'

'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

import sys

def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return

    number = ['0'] * n
    while not Increment(number):
        PrintNumber(number)


def Increment(number):
    isOverflow = False
    nTakeOver = 0
    nLength = len(number)

    for i in range(nLength - 1, -1, -1): #注意:这里的参数列表，第一个是开始，第二个是结束，第三个是步长
        nSum = int(number[i]) + nTakeOver #加上进位
        if i == nLength - 1:  # 如果是最低位
            nSum += 1 # 每次加一

        if nSum >= 10: # 如果个位加到满10了，应该向高位进1了
            if i == 0: # 如果是成立的，那么当前已经是最高位了，说明，可以停止遍历了
                isOverflow = True
            else:
                nSum -= 10 # 求出进位之后的低位的数字
                nTakeOver = 1 # 存放进一的记录 等下次循环计算nSum = int(number[i]) + nTakeOver
                number[i] = str(nSum)  # 当前位置的数字
        else:
            number[i] = str(nSum) # 如果不用进一，那么我们直接改变该位置的数字
            break

    return isOverflow


def PrintNumber(number):
    isBeginning0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            # print ''.join('%c' % number[i])
            sys.stdout.write('%c' % number[i])
    sys.stdout.write(" ")
    # Print1ToMaxOfNDigits(2)

def Print1ToMaxOfNDigits2(n):
    if n <= 0:
        return

    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, n, 0)

def Print1ToMaxOfNDigitsRecursively(number, length, index):
    if index == length - 1:
        PrintNumber(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, length, index + 1)



if __name__ == '__main__':
    # Print1ToMaxOfNDigits(2)
    Print1ToMaxOfNDigits2(2)
