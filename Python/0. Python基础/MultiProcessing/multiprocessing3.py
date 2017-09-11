# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 12:42'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'multiprocessing3.py'

import multiprocessing as mp
import threading as td
import time


# 代码案例：分别采用多进程，多线程，正常方法计算job
# 观察在这个过程中，我们使用的总的时间是多少
# 在电脑上通过运行，有以下输出
# ('normal:', 499999666667166666000000L)
# ('normal time:', 4.091000080108643)
# ('multithread:', 499999666667166666000000L)
# ('multithread time:', 4.517999887466431)
# ('multicore:', 499999666667166666000000L)
# ('multicore time:', 2.2179999351501465)
# 可以发现多线程的时候比正常运行的用时还要长的多
# 那么，其实使用多线程的时候是存在短板的
# 至于是什么短板，我们将在下一个程序中指出来
def job(q):
    res = 0
    for i in range(1000000):
        res += i + i ** 2 + i ** 3
    q.put(res)  # queue


def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)


def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    print('normal:', res)


def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)


if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)
