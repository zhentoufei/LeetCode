# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 10:08'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'threading3.py'

# Python通过两个标准库thread和threading提供对线程的支持。
# thread提供了低级别的、原始的线程以及一个简单的锁。
# threading基于Java的线程模型设计。
# 锁（Lock）和条件变量（Condition）在Java中是对象的基本行为（每一个对象都自带了锁和条件变量），而在Python中则是独立的对象。
# start_new_thread()要求一定要有前两个参数。所以，就算我们想要运行的函数不要参数，我们也要传一个空的元组

import threading
import time
import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


# 多线程中不能返回一个值哦

def multithreading():
    q = Queue.Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [5, 5, 5], [6, 6, 6]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print results


if __name__ == '__main__':
    multithreading()
