# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/12 19:50'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '55.字符流中第一个不重复的字符.py'


class Solution:
    def __init__(self):
        self.a_dict = {}
        self.a_list = []

    def firstAppearingOnce(self):
        while len(self.a_list) > 0 and self.a_dict[self.a_list[0]] == 2:
            self.a_list.pop(0)

        if len(self.a_list) == 0:
            return '#'
        else:
            return self.a_list[0]

    def insert(self, char):
        if char not in self.a_dict.keys():
            self.a_dict[char] = 1
            self.a_list.append(char)
        elif self.a_dict[char]:
            self.a_dict[char] = 2


if __name__ == '__main__':
    pass
