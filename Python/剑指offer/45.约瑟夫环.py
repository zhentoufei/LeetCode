# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/7 22:05'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '45.约瑟夫环.py'


def getRes(N, k):
    if N <= 0 or k <= 0:
        return []

    man = [0] * N
    count = 0
    i = 0
    pos = -1
    alive = 0
    while count <= N:
        while True:
            pos = (pos + 1) % N # 环状处理
            if man[pos] == 0:
                i += 1

            if i == k:
                i =0
                break
        man[pos] = count
        # 打印最后剩下的那个人的编号
        # if count == N:
        #     print pos
        count += 1

    # for i, val in enumerate(man):
    #     print i, ' ', val
    return man



if __name__ == '__main__':
    print getRes(3,3)
