# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/6 21:44'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '42.左旋转字符串.py'


class Solition:


    def Reverse(self, arr, start, end):
        if arr == None or len(arr) <= 0:
            return []

        start = start
        end = end
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def LsftRotateArr(self, arr_in, n):
        arr = list(arr_in)
        if arr == None or len(arr) <= 0 or n<0:
            return []

        self.Reverse(arr, 0, len(arr) -1 )
        self.Reverse(arr, 0, len(arr) - n -1)
        self.Reverse(arr, len(arr) - n, len(arr)-1)
        return arr

if __name__ == '__main__':
    print Solition().LsftRotateArr("abcdefg", 2)