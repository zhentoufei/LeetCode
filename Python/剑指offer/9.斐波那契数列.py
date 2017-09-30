# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/30 15:22'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '9.斐波那契数列.py'


# 使用lambda表达式实现斐波那契数列
def method_1():
    fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
    return fib


def memo(func):
    cache = {}

    def wrap(args):
        if args not in cache:
            cache[args] = func(args)
        return cache[args]

    return wrap


@memo
def method_2(n):
    if n < 2:
        return 1
    return method_2(n - 1) + method_2(n - 2)


# 不带中间变量的斐波那契数列
def method_3(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b


# 和方法3很类似，只不过这里使用的是数组，而且优化到只有两个元素的数组，
# 这个思想在背包问题里面也有被使用哦
def method_4(n):
    temp_arr = []
    if n >= 2:
        for i in xrange(2, n + 1):
            temp_arr[i % 2] = temp_arr[0] + temp_arr[1]
    return temp_arr[n % 2]


# 青蛙跳台阶，每次能跳1次或者两次
def junmpFloor(number):
    tmp_arr = [1, 2]
    if number >= 3:
        for i in xrange(3, number + 1):
            tmp_arr[(i + 1) % 2] = tmp_arr[0] + tmp_arr[1]
    return tmp_arr[(number + 1) % 2]


if __name__ == '__main__':
    print method_1()(4)
    print method_2(4)
    print method_3(4)
