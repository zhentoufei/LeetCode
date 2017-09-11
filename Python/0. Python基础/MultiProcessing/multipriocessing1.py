# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 12:24'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'multipriocessing1.py'

import multiprocessing as mp
import threading as td


def job(a, b):
    print 'a'


def test():
    # 进程和线程的操作是完全一样的，start和join的功能也是一摸一样的
    t1 = td.Thread(target=job, args=(1, 2))
    p1 = mp.Process(target=job, args=(1, 2))
    t1.start()
    p1.start()
    t1.join()
    p1.join()


if __name__ == '__main__':
    pass
