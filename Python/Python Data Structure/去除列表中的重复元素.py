# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/9/24 21:52'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '去除列表中的重复元素.py'

# 【去除列表中的重复元素】

def method_1(input_list):
    return list(set(input_list))


# 简单的使用字典
def method_2(input_list):
    return {}.fromkeys(input_list).keys()

# 使用字典并保持顺序
def method_3(input_list):
    tmp_list = list(set(input_list))
    tmp_list.sort(key=input_list.index)
    return tmp_list

# 列表推导
# 才发现if 1 not in a:和if not 1 in a:是一样的啊
def method_4(input_list):
    tmp_list = []
    return [tmp_list.append(i) for i in input_list if not i in tmp_list]


if __name__ == '__main__':
    a  = [2,3]
    if 1 not in a:
        print "a"
    if not 1 in a:
        print "b"
