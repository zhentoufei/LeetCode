# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 14:55'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'multiprocessing5.py'


import multiprocessing as mp

value = mp.Value('d', 1) # 前面的表示数据类型，d表示double，i表示int，这个是共享的内存,
array = mp.Array('i', [1,2,3]) # 区别与numpy的array，只能是一维的数据，如果是[[1,2,3]]是会报错的


if __name__ == '__main__':
    pass
