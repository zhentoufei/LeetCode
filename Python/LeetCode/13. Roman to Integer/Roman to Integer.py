# -*- coding:utf-8 -*-
# Time:  O(n)
# Space: O(1)
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the xrange from 1 to 3999.
#
# 不管怎么说，话是要祭出规则
# 其次，罗马数字转阿拉伯数字规则（仅限于3999以内）：
#
# 从前向后遍历罗马数字，如果某个数比前一个数小，则加上该数。反之，减去前一个数的两倍然后加上该数
class Solution:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in xrange(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == "__main__":
    # print Solution().romanToInt("CMXCIX")
    print Solution().romanToInt("IIVX")