# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 12:30'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'multiprocessing2.py'

import multiprocessing as mp


# 利用Queue来进行多进程值的计算的结合
# 和线程一样，我们不会在进程的job中有return值
def job(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)


if __name__ == '__main__':
    q = mp.Queue()
    # 注意：这里的args=(q,)，要在参数中添加一个逗号，表明参数是一个可迭代的对象
    # 如果在函数的输入参数是一个的时候，我们不加这个逗号，就会报错
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print res1 + res2
