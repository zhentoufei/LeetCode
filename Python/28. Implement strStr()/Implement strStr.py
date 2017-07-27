# Time:  O(n + k)
# Space: O(k)
#
# Implement strStr().
#
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#

# Wiki of KMP algorithm:
# http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        return self.KMP(haystack, needle)

    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        for i in xrange(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1

    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            prefix[i] = j
        print prefix
        return prefix

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1


# Time:  O(n * k)
# Space: O(k)
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


class Solution3(object):
    def strStr(self, haystack, needle):
        i_h = 0
        i_n = 0
        while i_h < len(haystack) and i_n < len(needle):
            if not haystack:
                print 'haystack'
                return -1
            if not needle:
                print 'needle'
                return -1
            if haystack[i_h] == needle[i_n]:
                if i_n == len(needle) - 1:
                    return i_h - i_n
                i_h += 1
                i_n += 1
            else:
                i_h = i_h - i_n + 1
                i_n = 0
        return -1


class Solution4(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nn = len(haystack)
        mm = len(needle)
        if haystack == needle:
            return 0
        for ii in range(nn):
            if ii + mm > nn:
                break
            if haystack[ii:ii + mm] == needle:
                return ii
        return -1


if __name__ == "__main__":
    # print Solution3().strStr("a", "")
    print Solution().strStr("abababcdab", "aaaabaa")
