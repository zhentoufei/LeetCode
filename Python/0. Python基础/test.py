# coding:utf-8
from itertools import chain
from random import randint
# 例子1
for x in chain([1, 2, 3, 4], ['a', 'b', 'c']):
    print x
    # 输出1 2 3 4 a b c


e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(22)]
e3 = [randint(60, 100) for _ in xrange(33)]
e4 = [randint(60, 100) for _ in xrange(55)]
count = 0
for s in chain(e1, e2, e3, e4):
    if s > 90
        count += 1

print count