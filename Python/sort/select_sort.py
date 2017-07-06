
def select_sort(nums):
    for i in range(0, len(nums)-1, 1):
        min_index = i
        for j in range(i+1, len(nums), 1):
            if nums[j]<nums[j-1]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
