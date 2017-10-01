# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/29 16:58'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '拓扑排序.py'


def indegree0(v, e):
    if v == []:
        return None
    tmp = v[:]
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp == []:
        return -1

    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i] = 'toDel'  # 占位，之后删掉
    if e:
        eset = set(e)
        eset.remove('toDel')
        e[:] = list(eset)
    if v:
        for t in tmp:
            v.remove(t)
    return tmp


def topoSort(v, e):
    result = []
    while True:
        nodes = indegree0(v, e)
        if nodes == None:
            break
        if nodes == -1:
            print('there\'s a circle.')
            return None
        result.extend(nodes)
    return result


if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e', 'f', 'o']
    e = [('a', 'b'), ('a', 'c'),
         ('b', 'd'), ('b', 'e'), ('c', 'e'), ('c', 'f'),
         ('d', 'o'), ('e', 'o'), ('f', 'o')]
    res = topoSort(v, e)
    print(res)
