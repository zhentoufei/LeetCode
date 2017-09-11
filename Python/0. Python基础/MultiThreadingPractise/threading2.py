# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/11 9:46'
__site__ = ''
__software__ = 'PyCharm'
__file__ = 'threading2.py'

import threading
import time
##############################################################
# 这种情况下，会在主线程结束后子线程才会结束
#
# def thread_job():
#     print "T1 start\n"
#     for i in range(10):
#         time.sleep(0.1)
#     print "T1 finished\n"
#
#
# def main():
#     added_thread = threading.Thread(target=thread_job, name='T1')
#     added_thread.start()
#     print 'all done\n'
##############################################################

def thread_job():
    print "T1 start\n"
    for i in range(10):
        time.sleep(0.1)
    print "T1 finished\n"

def T2_job():
    print 'T2 start\n'
    print 'T2 finished\n'


def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    thread2.start()
    thread2.join() # 在join后面的代码会在added_thread执行完毕后才会执行,而且并不会例会added_thread的东西
    print 'all done\n'


if __name__ == '__main__':
    main()
