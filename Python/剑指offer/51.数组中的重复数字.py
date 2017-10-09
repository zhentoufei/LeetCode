# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/9 9:01'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '51数组中重复的数字.py'


class Solution:
    def isDupl(self, arr):

        length = len(arr)
        if arr == None or len(arr) == 0:
            return False

        for i in arr:
            if i < 0 or i > length - 1:
                return False

        for i in xrange(length):
            while arr[i] != i:
                if arr[i] == arr[arr[i]]:
                    return True
                arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
        return False


if __name__ == '__main__':
    pass
