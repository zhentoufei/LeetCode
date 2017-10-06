# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/6 21:28'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '42.翻转单词顺序.py'


class Solution:

    def reverseSentence(self, s):
        if s == None or len(s) <=0:
            return ''

        str_list = list(s)
        str_list = self.reverse(str_list)
        start = 0
        end = 0
        res_str = ''
        res_tmp = []

        while end < len(s):

            if end == len(s) -1:
                res_tmp.append(self.reverse(str_list[start:]))
                break

            if str_list[start] == ' ':
                start += 1
                end += 1
                res_tmp.append(' ')
            elif str_list[end] == ' ':
                res_tmp.append(self.reverse(str_list[start:end]))
                start = end
            else:
                end += 1

        for i in res_tmp:
            res_str += ''.join(i)
        return res_str


    def reverse(self, arr):
        if arr == None or len(arr) <= 0:
            return ''

        start = 0
        end = len(arr)-1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

class Soltion2:
    def pythonicReverse(self, arr):
        l = arr.split(' ')
        return ' '.join(l[::-1])


if __name__ == '__main__':
    print Soltion2().pythonicReverse('i am a boy!')