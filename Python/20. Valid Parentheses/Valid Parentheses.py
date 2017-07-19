# -*- coding:utf-8 -*-
# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

# most least time consumption, but i dont know why
class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for parenth in s:
            if parenth in dict:
                stack.append(parenth)
            elif len(stack) == 0 or dict[stack.pop()] != parenth:
                return False

        return len(stack) == 0

if __name__ == "__main__":
    print Solution().isValid("([])[]{}")
    print Solution().isValid("()[{]}")