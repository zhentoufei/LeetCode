# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 15:51'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '24.二叉搜索树的后续遍历序列.py'


class Solution:
    def VerifySquenceOfBST(self, sequence, start, length):
        if sequence == [] or length <= 0:
            return False

        root = sequence[length - 1]
        i = 0
        while i < length - 1:
            if sequence[i] > root:
                break
            i += 1
        j = i
        while j < length - 1:
            if sequence[j] < root:
                return False
            j += 1
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence, 0, i)
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence, i + 1, length - i - 1)
        return (left and right)


if __name__ == '__main__':
    array = [5, 7, 6, 9, 11, 10, 8]
    # array2 = [4, 6, 7, 5]
    array2 = [7, 4, 6, 5]

    array3 = [1, 2, 3, 4, 5]
    S = Solution()
    print(S.VerifySquenceOfBST(array, 0, len(array)))
    print(S.VerifySquenceOfBST(array2, 0, len(array2)))
    print(S.VerifySquenceOfBST(array3, 0, len(array3)))
