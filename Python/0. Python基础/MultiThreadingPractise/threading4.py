# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 10:25'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'thread4.py'

import threading
import Queue
import copy
import time

#Global Interpreter Lock
#                      I/O            I/O             I/O
#                        (GIL)release->|<-acquire(GIL)
# Thread 1 ->>>>run>>>>-|--------------|---------------|-->>>>run>>>>--------
#                       |              |               |
#                       |              |               |
# Thread 2 -------------|-->>>>run>>>>-|---------------|---------------------
#                       |              |               |
#                       |              |               |
# Thread 3 -------------|--------------|-->>>>run>>>>--|---------------------
#                       |              |               |
#         (GIL)release->|<-acquire(GIL)  (GIL)release->|<-acquire(GIL)
# 从上图可以看出，在python中由于全局解释器锁的存在，程序在每个时刻只有一个线程在进行一步计算操作

def job(l, q):


    res = sum(l)
    q.put(res)
    if threading.current_thread().getName() == 'T0':
        time.sleep(1)
        print 'I am sleeping'
    print 'thread', threading.current_thread().getName()

def multithreading(l):
    q = Queue.Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    total = sum(l)
    print(total)


if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l * 4)
    print('normal: ', time.time() - s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time() - s_t)
