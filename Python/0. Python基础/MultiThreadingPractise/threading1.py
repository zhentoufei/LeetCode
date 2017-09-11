# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 9:38'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'threading1.py'

import threading

def thread_job():
    print "This is an added thread, number is %s"%threading.current_thread()


def test():
    add_thread = threading.Thread(target=thread_job)
    add_thread.start()
    print threading.active_count() # 查看被激活的线程数目
    print threading.enumerate() # 查看激活线程的详细信息
    print threading.current_thread() #查看当前运行的线程


if __name__ == '__main__':
    test()