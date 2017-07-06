# coding: utf-8

def inset_sort(nums):
    for i in range(1, len(nums), 1):
        for j in range(i, 0, -1):
            if nums[j]<nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else: # 注意这里
                break
    # for i in range(0, len(nums)-1, 1):
    #     for j in range(i+1, 0, -1):
    #         if nums[j]<nums[j-1]:
    #             nums[j], nums[j-1] = nums[j-1], nums[j]
    #         else: # 注意这里
    #             break
    return nums
