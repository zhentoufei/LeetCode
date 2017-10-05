# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/5 20:35'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '数字在排序数组中出现的次数.py'

'''
面试题38：数字在排序数组中出现的次数：二分查找的扩展。可以构造两个函数。
第一个函数查找目标数字出现的最前面的位置，先使用二分查找找到该数字，如果该数字的index > 0
而且该数字前面一个数字等于k的话，那么就令end=middle-1，继续二分查找。对于第二个函数，
查找目标数字出现的最后面的位置，反之编写。最后如果数字存在的话，令走后面的index减去最前面的index然后+1即可。
在进行有序数组的元素查找，可以先尝试一下二分查找
'''


class Solution:
    def getNumberOfK(self, data, k):
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.getFirstK(data, length, k, 0, length - 1)
            last = self.getLastK(data, length, k, 0, length - 1)
            if first > -1:
                number = last - first + 1
            return number

    # [start, ..., end]是闭区间上的
    def getFirstK(self, data, length, k, start, end):
        if start > end:
            return -1

        mid_index = (start + end) / 2
        mid_data = data[mid_index]

        if mid_data == k:
            if mid_index > 0 and data[mid_index - 1] == k:
                end = mid_index - 1
            else:
                return mid_index
        elif mid_data > k:
            end = mid_index - 1
        else:
            start = mid_index + 1
        return self.getFirstK(data, length, k, start, end)

    # [start, ..., end]是闭区间上的哦
    def getLastK(self, data, length, k, start, end):
        if start > end:
            return -1

        mid_index = (start + end) / 2
        mid_data = data[mid_index]

        if mid_data == k:
            if mid_index < end and data[mid_index + 1] == k:
                start = mid_index + 1
            else:
                return mid_index
        elif mid_data > k:
            end = mid_index - 1
        else:
            start = mid_index + 1
        return self.getLastK(data, length, k, start, end)


if __name__ == '__main__':
    alist = [3, 3, 3, 3, 4, 5]
    s = Solution()
    print(s.getNumberOfK(alist, 3))
