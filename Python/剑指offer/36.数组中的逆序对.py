# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 22:13'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '36.数组中的逆序对.py'

'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''


def inversePairs(data):
    length = len(data)
    if data == None or length <= 0:
        return 0
    copy = [0] * length
    for i in range(length):
        copy[i] = data[i]

    # 这里的是闭区间哦 [0,..., length-1]
    count = inversePairsCore(data, copy, 0, length - 1)
    return count


def inversePairsCore(data, copy, start, end):
    if start == end:
        copy[start] = data[start]
        return 0
    length = (end - start) / 2
    left = inversePairsCore(copy, data, start, start + length)
    right = inversePairsCore(copy, data, start + length + 1, end)

    # i初始化为前半段最后一个数字的下标
    i = start + length

    # j初始化为后半段最后一个数字的下标
    j = end

    index_copy = end
    count = 0

    while i >= start and j >= start + length + 1:
        if data[i] > data[j]:
            copy[index_copy] = data[i]
            index_copy -= 1
            i -= 1
            count += j - start - length
        else:
            copy[index_copy] = data[j]
            index_copy -= 1
            j -= 1
    while i >= start:
        copy[index_copy] = data[i]
        index_copy -= 1
        i -= 1

    while j >= start + length + 1:
        copy[index_copy] = data[i]
        index_copy -= 1
        j -= 1

    return left + right + count


# 方法二：使用数据的index进行求解
def inversePairs2(data):
    if len(data) <= 0:
        return 0

    count = 0
    copy = []
    for i in range(len(data)):
        copy.append(data[i])

    copy.sort()
    i = 0

    while len(copy) > i:
        count += data.index(copy[i])
        data.remove(copy[i])
        i += 1
    return count


if __name__ == '__main__':
    a = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505,
         360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162,
         268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478,
         147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235,
         187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
    b = [1, 2, 0]
    print inversePairs2(b)
