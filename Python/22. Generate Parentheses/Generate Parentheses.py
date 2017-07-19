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


#
# 所谓Backtracking都是这样的思路：在当前局面下，你有若干种选择。那么尝试每一种选择。
# 如果已经发现某种选择肯定不行（因为违反了某些限定条件），就返回；如果某种选择试到最后发现是正确解，就将其加入解集
#
# 所以你思考递归题时，只要明确三点就行：选择 (Options)，限制 (Restraints)，结束条件 (Termination)。
#
# 对于这道题，在任何时刻，你都有两种选择：
# 1. 加左括号。
# 2. 加右括号。
#
# 同时有以下限制：
# 1. 如果左括号已经用完了，则不能再加左括号了。
# 2. 如果已经出现的右括号和左括号一样多，则不能再加右括号了。因为那样的话新加入的右括号一定无法匹配。
#
# 结束条件是：
# 左右括号都已经用完。
#
# 结束后的正确性：
# 左右括号用完以后，一定是正确解。因为1. 左右括号一样多，2. 每个右括号都一定有与之配对的左括号。因此一旦结束就可以加入解集（有时也可能出现结束以后不一定是正确解的情况，这时要多一步判断）。
#
# 递归函数传入参数：
# 限制和结束条件中有“用完”和“一样多”字样，因此你需要知道左右括号的数目。
# 当然你还需要知道当前局面sublist和解集res。
class Solution3(object):
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

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens.append(p)
            return parens

        return generate('', n, n)


# 36ms的解决方案-太绕了，还是看看上面的递归吧
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
    print Solution2().generateParenthesis(2)