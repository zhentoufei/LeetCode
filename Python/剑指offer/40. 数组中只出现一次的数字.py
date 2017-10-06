# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/6 20:18'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '40. 数组中只出现一次的数字.py'

'''
题目：一个整形数组里面，除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现了一次的数字。
要求时间复杂度是O(n),空间复杂度O(1)

任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数。数组中出了两个数字之外，其他数字都出现两次，
那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵消掉，那两个不同的数字异或的值不为0，
也就是说这两个数的异或值中至少某一位为1。我们找到结果数字中最右边为1的那一位i，然后一次遍历数组中的数字，
如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。这样任何两个相同的数字就分到了一组，
而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，然后再对两个组依次进行异或操作，
最后每一组得到的结果对应的就是两个只出现一次的数字。
'''

class Solution1:
    def findNumAppearOnce(self, arr):
        if arr == None and len(arr):
            return []
        res_exclusive_or = 0
        for i in arr:
            res_exclusive_or ^= i

        index_of_1 = self.find1stBitIs1(res_exclusive_or)

        num_1 = 0
        num_2 = 0
        for j in xrange(len(arr)):
            if self.isBit1(arr, index_of_1):
                num_1 ^= arr[j]
            else:
                num_2 ^= arr[j]
        return [num_1, num_2]

    # 找到二进制数中的从低位往高位数，第一个是1的位置索引
    def find1stBitIs1(self, num):
        index = 0
        while num & 1 == 0 and index <= 32:
            index += 1
            num = num >> 1
        return index

    def isBit1(self, num, index):
        num = num >> index
        return num & 1


if __name__ == '__main__':
    print Solution1().find1stBitIs1(6)