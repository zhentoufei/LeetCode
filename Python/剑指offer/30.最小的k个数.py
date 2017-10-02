# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/10/2 16:30'
__site__ = ''
__software__ = 'PyCharm'
__file__ = '30.最小的k个数.py'

'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

两种方法。第一种方法是基于划分的方法，如果是查找第k个数字，第一次划分之后，划分的位置如果大于k，
那么就在前面的子数组中进行继续划分，反之则在后面的子数组继续划分，时间复杂度O(n)；

第二种方法是可以适用于海量数据的方法，该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，
然后从第k+1个数字开始遍历数组，如果遍历到的元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，
最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。
'''

# ===========================================================================
# 方法1：复杂度O(n)
def getLeastKthNumber(nums, kth):
    if nums == None or len(nums) < kth or kth <= 0:
        return []

    length = len(nums)
    start = 0
    end = length - 1
    index = partition(nums, length, start, end)
    while index != kth-1:
        if index > kth-1:
            end = index -1
            index = partition(nums, length, start, end)
        else:
            start = index +1
            index = partition(nums, length, start, end)
    res = nums[:kth] # 注意：经过上面的步骤之后我们的数组已经排好顺序了
    return res



# 闭区间[start, ..., end]，返回当前数字躲在的索引
def partition(nums, lenght, start, end):
    if nums == None or lenght <= 0 or start < 0 or end >= lenght:
        return None

    pivot_val = nums[start]
    left = start + 1
    right = end

    while True:

        while nums[left] <= pivot_val and left <= end:
            left += 1
        while nums[right] >= pivot_val and right >= start + 1:
            right -= 1

        if left > right:
            break
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right += 1
    nums[start], nums[right] = nums[right], nums[start]
    return right


#============================================================================
# 方法2：O(nlogk)的复杂度，适合处理海量的数据

def getLeastKthNumbers(nums, kth):
    import heapq
    if nums == None or len(nums) == 0 or len(nums) < kth or kth <= 0:
        return []

    res = []
    for num in nums:
        if len(res) < kth:
            res.append(num)
        else:
            res = heapq.nlargest(kth, res) # 将res做了从大到小的排序
            if num > res[0]:
                continue
            else:
                res[0] = num
    return res[::-1] # 从小到大输出




if __name__ == '__main__':
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    print(getLeastKthNumbers(tinput, 4))
    # print(getLeastKthNumber(tinput, 4))
    # print(getLeastKthNumber(tinput, 5))
