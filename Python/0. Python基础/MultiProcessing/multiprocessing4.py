# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 12:55'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'multiprocessing4.py'

# 在使用线程池的时候，我们可以是哟return了
import multiprocessing as mp


def job(x):
    return x * x


def multiccor():
    pool = mp.Pool(processes=2)  # 设置使用的核心数目是2
    # pool = mp.Pool() #默认情况下是本机电脑的所有的核心数目

    # map可以传入很多可迭代参数，并且将这些参数自动分配给这些进程
    res = pool.map(job, range(10))
    print res

    # 除了map的功能我们还有apply_async的操作，但是这个操作一般只能传入一个参数，并将这个参数传入到一个核心上进行相应的此操作

    # apply_async一次只能把一个东西传送给一个函数
    res1 = pool.apply_async(job, (1,))
    # res1 = pool.apply_async(job, (1,2,3,4)) #这种情况会导致错误
    print res1

    res2 = [pool.apply_async(job, (i,)) for i in range(10)]
    print [res.get() for res in res2]


if __name__ == '__main__':
    multiccor()
