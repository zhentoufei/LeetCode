# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/24 20:49'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '斐波那契.py'


def method_1():
    fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
    return fib


def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def method_2(i):
    if i < 2:
        return 1
    return method_2(i - 1) + method_2(i - 2)


def method_3(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print method_3(5)
