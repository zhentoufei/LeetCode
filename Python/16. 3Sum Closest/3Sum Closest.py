# -*- coding:utf-8 -*-
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = float('inf')
        min_diff = float('inf')
        i = 0
        while i < len(nums) - 2:
            # 阶段1
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    # 阶段2
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                    result = nums[i] + nums[j] + nums[k]
                    # 阶段3
                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return result
            i += 1
        return result

if __name__ == '__main__':
    result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print result