# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/1 13:46'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '20.顺时针打印矩阵.py'

'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''


class Solution:
    def printMatrix(self, matrix):
        if matrix == None:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while rows > start * 2 and cols > start * 2:
            self.printMatrixInCircle(matrix, cols, rows, start)
            start += 1

    def printMatrixInCircle(self, matrix, cols, rows, start):
        end_x = cols - 1 - start
        end_y = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, end_x + 1):
            number = matrix[start][i]
            print number,

        # 从上到下打印一列
        if start < end_y:
            for i in range(start + 1, end_y + 1):
                number = matrix[i][end_x]
                print number,

        # 从右到左打印一列
        if start < end_x and start < end_y:
            for i in range(end_x - 1, start - 1, -1):
                number = matrix[end_y][i]
                print number,
        # 从下往上
        if start < end_x and start < end_y - 1:
            for i in range(end_y - 1, start, -1):
                number = matrix[i][start]
                print number,


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix2 = [[1], [2], [3], [4], [5]]
    matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    S = Solution()
    S.printMatrix(matrix)
    # S.printMatrix(matrix2)
    # S.printMatrix(matrix3)
