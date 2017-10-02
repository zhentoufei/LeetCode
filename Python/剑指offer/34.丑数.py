# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 20:28'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '34.丑数.py'


def getUglyNu(index):
    if index == None and index <= 0:
        return 0

    ugly_nums = [1] * index
    next_index = 1

    index_2 = 0
    index_3 = 0
    index_5 = 0

    while next_index < index:
        min_val = min(ugly_nums[index_2] * 2,
                      ugly_nums[index_3] * 3,
                      ugly_nums[index_5] * 5)
        ugly_nums[next_index] = min_val

        while ugly_nums[index_2]*2 <= ugly_nums[next_index]:
            index_2 += 1

        while ugly_nums[index_3]*3 <= ugly_nums[next_index]:
            index_3 += 1

        while ugly_nums[index_5]*5 <= ugly_nums[next_index]:
            index_5 += 1

        next_index += 1

    return ugly_nums[-1]

if __name__ == '__main__':
    print(getUglyNu(11))
