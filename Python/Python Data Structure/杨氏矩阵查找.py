# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/24 21:34'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '杨氏矩阵查找.py'

# 【杨氏矩阵查找】
# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 使用Step - wise线性搜索。

def find(metrx, target):
    len_row = len(metrx) - 1
    len_col = len(metrx[0]) - 1
    index_row = 0
    index_col = len_col
    while index_col >= 0 and index_row <= len_row:
        val = metrx[index_row][index_col]
        if val == target:
            return True
        elif target < val:
            index_col -= 1
        elif target > val:
            index_row += 1
    return False


if __name__ == '__main__':
    matrix = [[1,2], [3,4]]
    print find(matrix, 3)
