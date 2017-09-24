# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 10:54'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'threading5.py'

import threading

def job_1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print 'Job_1', A
    lock.release()

def job_2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print 'Job_2', A
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job_1)
    t2 = threading.Thread(target=job_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()