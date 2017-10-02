# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 11:32'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '28.字符串的排列.py'

'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

# 方法一：递归，该方法适用不重复的,如果有重复的，那么我们就先去重再操作
res = []


def myPermutation(in_list):
    if len(in_list) == 0:
        return res

    used = [False] * len(in_list)
    genPermutaion(in_list, 0, "", used)
    return res


def genPermutaion(in_list, index, tmp_res, used):
    if index == len(in_list):
        res.append(tmp_res)
        return

    for i in range(len(in_list)):
        if used[i] == False:
            used[i] = True
            tmp_res += in_list[i]
            genPermutaion(in_list, index + 1, tmp_res, used)
            tmp_res = tmp_res[:-1]
            used[i] = False
    return


# 方法二：这种方法不会产生重复额，比如输入['1', '1'],那么输出只有['11']
def Permutation(ss):
    if not len(ss):
        return []
    if len(ss) == 1:
        return list(ss)

    charList = list(ss)
    charList.sort()
    pStr = []
    for i in range(len(charList)):
        if i > 0 and charList[i] == charList[i - 1]:
            continue
        print ''.join(charList[:i]) + ''.join(charList[i + 1:])
        temp = Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))
        for j in temp:
            pStr.append(charList[i] + j)
    return pStr

# 扩展习题, 生成字符的所有组合
# 比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合
def group(ss):
    if not len(ss):
        return []
    if len(ss) == 1:
        return list(ss)
    charList = list(ss)
    charList.sort()
    pStr = []
    for i in range(len(charList)):
        if i > 0 and charList[i] == charList[i - 1]:
            continue
        pStr.append(charList[i])
        temp = group(''.join(charList[i + 1:]))
        for j in temp:
            pStr.append(charList[i] + j)
        pStr = list(pStr)
        pStr.sort()
    return pStr



if __name__ == '__main__':
    print myPermutation(['1', '2'])
    print group(['1', '2', '3', '1'])
