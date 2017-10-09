# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/9 20:19'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '最长重复子串.py'


def slice_window(str_list, n):
    '''''
    滑窗切片操作
    '''
    result_list = []
    for i in range(0, len(str_list) - n + 1, n):
        result_list.append('/'.join(str_list[i:i + n]))
    return result_list


def find_repeat_pattern(str_in):
    str_list = list(str_in)
    result_list = []
    result_dict = {}
    for i in range(2, len(str_list)):
        result_list += slice_window(str_list, i)
    for one in result_list:
        if one in result_dict:
            result_dict[one] += 1
        else:
            result_dict[one] = 1

    return result_dict


def find_real_pattern(result_dict):
    new_result_dict = {}
    keys_list = result_dict.keys()
    for i in range(len(keys_list)):
        first = keys_list[i]
        for j in range(len(keys_list)):
            second = keys_list[j]
            if first in second and first != second and result_dict[first] > 1 and result_dict[second] > 1:
                new_result_dict[keys_list[j]] = result_dict[keys_list[j]]
    return new_result_dict


if __name__ == '__main__':
    # str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '4', '3', '4', '3', '4', '3', '4', '3', '4', '3']

    str_list = '123456784343434343'
    result_dict = find_repeat_pattern(str_list)
    for k, val in result_dict.iteritems():
        if val > 1:
            print k, ' ', val

    # print find_real_pattern(result_dict)

