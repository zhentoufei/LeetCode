# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 15:39'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'multiprocessing6.py'

import multiprocessing as mp
import time


# def job(v, num):
#     for _ in range(10):
#         time.sleep(1)
#         v.value += num
#         print v.value
#
#
# def multi_core():
#     v = mp.Value('i', 0)
#     p1 = mp.Process(target=job, args=(v,1))
#     p2 = mp.Process(target=job, args=(v,3))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


def job(v, num, lock):
    lock.acquire()
    for _ in range(10):
        time.sleep(1)
        v.value += num
        print v.value
    lock.release()

def multi_core():
    lock = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1, lock))
    p2 = mp.Process(target=job, args=(v, 3, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multi_core()
