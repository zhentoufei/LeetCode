# coding: utf-8
def bubble_sort(nums):
    for i in range(0, len(nums)-1, 1):
        for j in range(len(nums)-1, i, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums



def select_sort(nums):
    for i in range(0, len(nums)-1, 1):
        min_index = i
        for j in range(i+1, len(nums), 1):
            if nums[j]<nums[j-1]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

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


def shell(nums):
    step = len(nums) / 2
    while step > 0:
        for i in range(step, len(nums)):
            for j in range(i, step - 1, -1):
                print j
                if nums[j] < nums[j - step]:
                    nums[j], nums[j - step] = nums[j - step], nums[j]
                else:
                    break
        step = step / 2
    return nums


if __name__ == '__main__':
    nums = [9, 3, 5, 8, 2, 7, 1]
    print bubble_sort(nums)
