# -*- coding:utf-8 -*-
# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
import collections


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                # 从两边往中间找
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        # 防止结果中有重复的数据
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result
    
    # the solution of least time consumption
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dic = {}
        for x in nums:  # o(n)
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        uniq = dic.keys()
        pos = sorted(x for x in uniq if x >= 0)  # (o(nlogn))
        neg = sorted(x for x in uniq if x < 0)
        if 0 in dic and dic[0] >= 3:
            res.append([0, 0, 0])
        for p in pos:
            for n in neg:
                r = 0 - p - n
                if r in dic:
                    if (r == p or r == n) and dic[r] > 1:
                        res.append([n, r, p])
                    elif r < n:  # avoid same
                        res.append([r, n, p])
                    elif r > p:
                        res.append([n, p, r])
        return res

if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print result

