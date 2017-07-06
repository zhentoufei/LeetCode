# coding: utf-8

def shell_sort(nums):
    step = len(nums)/2
    while step>0:
        for i in range(step, len(nums), 1):
            for j in range(i, step-1, -1):
                if nums[j]<nums[j-step]:
                    nums[j], nums[j-step] = nums[j-step], nums[j]
                else:
                    break
        step = step/2
    return nums




def shellSort(nums):
    # 设定步长
    step = len(nums) / 2
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and nums[i - step] > nums[i]:
                nums[i], nums[i - step] = nums[i - step], nums[i]
                i -= step
        step = step / 2
    return nums
