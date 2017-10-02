# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 20:05'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '33.把数组排列成最小的数.py'

from functools import cmp_to_key


def PrintMinNumber(numbers):
    if numbers == None or len(numbers) <= 0:
        return ''
    strList = []
    for i in numbers:
        strList.append(str(i))
    # key是一种比较规则
    # 比较 x+y 和 x-y 的大小, 因为为str型, 需要先转换成int型
    key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
    strList.sort(key=key)
    print strList
    return ''.join(strList)


def PrintMinNumber2(numbers):
    if numbers == None or len(numbers) <= 0:
        return ''
    strNum = [str(m) for m in numbers]
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                strNum[i], strNum[j] = strNum[j], strNum[i]
    return ''.join(strNum)


if __name__ == '__main__':
    print PrintMinNumber([3, 32, 321])
    print PrintMinNumber2([3, 32, 321])
