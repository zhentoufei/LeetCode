# -*- coding:utf-8 -*-
# Time:  O(n^2 * p)
# Space: O(n^2 * p)
# Hash solution. (224ms)
import collections


class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                is_duplicated = False
                for [x, y] in lookup[nums[i] + nums[j]]:
                    if nums[x] == nums[i]:
                        is_duplicated = True
                        break
                if not is_duplicated:
                    lookup[nums[i] + nums[j]].append([i, j])
        ans = {}
        for c in xrange(2, len(nums)):
            for d in xrange(c + 1, len(nums)):
                if target - nums[c] - nums[d] in lookup:
                    for [a, b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = " ".join(str(quad))
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)
        return result

# 最高效的算法
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        if (n < 4):
            return result
        nums.sort()
        # basically two layers of loop
        # first loop is for first element and the element just after it
        # second loop is for the left and right pointers
        for i in xrange(n-3):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3]) > target:
                break
            if (nums[i] + nums[n-1] + nums[n-2] + nums[n-3]) < target:
                continue
            for j in xrange(i+1, n-2):
                if (j > i+1 and nums[j] == nums[j-1]):
                    continue
                if (nums[i] + nums[j] + nums[j+1] + nums[j+2]) > target:
                    break
                if (nums[i] + nums[j] + nums[n-2] + nums[n-1]) < target:
                    continue
                left,right = j+1, n-1
                while (left < right):
                    s = nums[i] + nums[j] + nums[left]+nums[right]
                    if (s > target):
                        right -= 1
                    elif (s < target):
                        left += 1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while (left < right and nums[left] == nums[left + 1]):
                            left += 1
                        while (left < right and nums[right] == nums[right-1]):
                            right -= 1
                        left += 1
                        right -= 1
        return result