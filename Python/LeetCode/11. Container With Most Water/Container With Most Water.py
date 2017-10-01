# -*- coding:utf-8 -*-
class Solution:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height)-1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    height = [1, 2, 3, 4, 3, 2, 1, 5]
    result = Solution().maxArea(height)
    print result
