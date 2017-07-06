def bubble_sort(nums):
    for i in range(0, len(nums)-1, 1):
        for j in range(len(nums)-1, i, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums
