# -*- coding:utf-8 -*-
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecu(result, current + ")", left, right - 1)


# 36ms的解决方案
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = []
        index = 1
        dp.append([""])
        while index < n+1:
            temp = []
            for i in range(index):
                for front in dp[i]:
                    for back in dp[len(dp) - i - 1]:
                        temp.append("(" + front + ")" + back)
            dp.append(temp)
            index += 1
        return dp[n]
if __name__ == "__main__":
    print Solution().generateParenthesis(2)