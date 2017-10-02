# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 21:11'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '35.第一个只出现一次的字符.py'

'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

def findNoRepeatChar(s):
    if s == None or len(s) <= 0:
        return -1

    alpha = {}
    a_list = list(s)
    for i in a_list:
        if i not in alpha.keys():
            alpha[i] = 0
        alpha[i] += 1

    for i in a_list:
        if alpha[i] == 1:
            return i

    return -1


if __name__ == '__main__':
    print findNoRepeatChar('asdfasdfv')