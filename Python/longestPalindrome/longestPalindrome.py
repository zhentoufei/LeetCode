# -*- coding:utf-8 -*-
class Solution(object):
    def longestStr(self, s, left, right):
        l = len(s)
        while left >= 0 and right < l and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""

        ret = "";
        i = 0
        for i in range(len(s) * 2 - 1):
            left = i / 2
            right = i / 2
            if (i & 1) == 1: right += 1

            tmp = self.longestStr(s, left, right)

            if len(tmp) > len(ret): ret = tmp

        return ret


    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """

        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T += ['#', c]
            T += ['#', '$']
            return T

        T = preProcess(s)
        P = [0] * len(T)
        center, right = 0, 0
        for i in xrange(1, len(T) - 1):
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i = 0
        for i in xrange(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) / 2
        return s[start: start + P[max_i]]


if __name__ == "__main__":
    print Solution().longestPalindrome("ab123sdasdasasdffdsab")
    print Solution().longestPalindrome_1("ab123sdasdasasdffdsab")