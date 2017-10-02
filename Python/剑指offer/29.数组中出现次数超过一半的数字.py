# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 13:57'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '29.数组中出现次数超过一半的数字.py'


def checkInvalidArr(nums, lenght):
    invalid = False
    if nums == None or lenght <= 0:
        invalid = True
    return invalid


def checkMoreThanHalf(nums, lenght, num):
    times = 0
    for ele in nums:
        if ele == num:
            times += 1
    if times << 2 <= lenght:
        return False
    return True


def partion(nums, length, start, end):
    if nums == None or length <= 0 or start < 0 or end >= length:
        return None
    if end == start:
        return end

    pivote_val = nums[start]
    left = start + 1
    right = end

    while True:
        while nums[left] < pivote_val and left <= end:
            left += 1
        while nums[right] > pivote_val and right >= start + 1:
            right -= 1

        if left > right:
            break
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    nums[right], nums[start] = nums[start], nums[right]
    return right


def MoreThanHalfNum(nums):
    length = len(nums)
    if length == 1:
        return nums[0]

    if checkInvalidArr(nums, length):
        return

    mid = length >> 1
    start = 0
    end = length - 1
    index = partion(nums, length, start, end)

    while index != mid:
        if index > mid:
            end = index - 1
            index = partion(nums, length, start, end)
        else:
            start = index + 1
            index = partion(nums, length, start, end)
    res = nums[mid]
    if not checkMoreThanHalf(nums, length, res):
        res = 0
    return res


# 方法二
def MoreThanHalfNum_2(nums):
    length = len(nums)
    if nums == None or length <= 0:
        return 0

    res = nums[0]
    times = 0
    for num in nums:
        if times == 0:
            res = num
            times = 1
        elif num == res:
            times += 1
        else:
            times -= 1

    if checkMoreThanHalf(nums, length, res) == False:
        res = 0
    return res


if __name__ == '__main__':
    # print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    # print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
    # print(S.MoreThanHalfNum_Solution([1, 2]))
    print(MoreThanHalfNum([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(MoreThanHalfNum([1, 2, 3, 3, 3, 3, 4]))
    print(MoreThanHalfNum([1, 2]))

    print(MoreThanHalfNum_2([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(MoreThanHalfNum_2([1, 2, 3, 3, 3, 3, 4]))
    print(MoreThanHalfNum_2([1, 2]))
