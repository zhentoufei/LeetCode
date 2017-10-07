# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/7 20:08'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '44.扑克牌的顺子.py'


class Solution:
    def isContinuous(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        tran_dict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in tran_dict.keys():
                numbers[i] = tran_dict[numbers[i]]

        numbers = sorted(numbers)
        number_of_0 = 0
        number_of_gap = 0

        # 统计0的个数
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            number_of_0 += 1
            i += 1

        # 统计间隔的数目
        small = number_of_0
        big = small + 1
        while big < len(numbers):

            if numbers[small] == numbers[big]:
                return False

            number_of_gap += numbers[big] - numbers[small] - 1
            small = big
            big += 1

        return False if number_of_gap > number_of_0 else True

class ListNode:
    def __init__(self, x= None):
        self.x = x
        self.next = None




if __name__ == '__main__':
    test = ['A', 3, 2, 5, 0]
    test2 = [0, 3, 1, 6, 4]
    s = Solution()
    print(s.isContinuous(test2))


