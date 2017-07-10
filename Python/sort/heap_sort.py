# -*- coding:utf-8 -*-
# version: 1.0

# 堆排序
import math


def swap_node(lst, i, lst_len):
    # 用来判断位置i的节点与其左右子节点相比是否最大/小，如果不是则交换为最大/小
    if lst_len > (i * 2):  # i节点有左右子节点
        if lst[i * 2] > lst[i * 2 + 1]:
            if lst[i * 2] > lst[i]:
                lst[i], lst[i * 2] = lst[i * 2], lst[i]
        else:
            if lst[i * 2 + 1] > lst[i]:
                lst[i], lst[i * 2 + 1] = lst[i * 2 + 1], lst[i]
    elif lst_len == (i * 2):  # i节点只有左子节点
        if lst[i] < lst[i * 2]:
            lst[i], lst[i * 2] = lst[i * 2], lst[i]
    else:  # i节点没有左子节点
        pass


def heap_adjust(lst, lst_len):
    # 堆调整，本例是将大数值调整到堆顶
    # 计算层数
    # lev = int(math.log(lst_len, 2)) + 1
    # for i in range(int(math.pow(2, lev-1)-1), 0, -1):
    #     swap_node(lst, i, lst_len)

    for i in range(int(lst_len / 2), 0, -1):
        swap_node(lst, i, lst_len)


def heap_sort(lst):
    # 堆排序
    lst_len = len(lst) - 1
    # 先做一次调整
    heap_adjust(lst, lst_len)

    # 循环每次讲堆顶元素和堆底元素对调，并重新调整
    for i in range(lst_len, 1, -1):
        lst[1], lst[i] = lst[i], lst[1]
        heap_adjust(lst, i - 1)


if __name__ == '__main__':
    # lst第一位为-1占位，不作排序
    lst = [-1, 1, 3, 6, 88, 67, 22, 99, 56, 88, 27, 160, 38, 12, 7, 72, 12, 63, 356, 26, 99, 66, 86]
    heap_sort(lst)
    print 'lst', lst
