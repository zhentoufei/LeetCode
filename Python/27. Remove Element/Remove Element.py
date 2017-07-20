# -*- coding:utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        last = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[last] = nums[i]
                last += 1
            i += 1
        return last
