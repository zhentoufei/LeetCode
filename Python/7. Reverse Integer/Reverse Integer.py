# -*- coding:utf-8 -*-
# Time:  O(logn) = O(1)
# Space: O(1)
#
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
# then the reverse of 1000000003 overflows. How should you handle such cases?
#
# Throw an exception? Good, but what if throwing an exception is not an option?
# You would then have to re-design the function (ie, add an extra parameter).


# 关于32bit整形的最大值的解释
# nt 占4个字节，32位。
# 四个二进制位对应一个十六进制数，二进制第一个是符号位。
# 所以最大的整型数是0x7fffffff。
# 如果是unsigned int ，最大数就是0xffffffff 。

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int

        关于[::-1]的注释
        将列表a倒序处理，如果a＝［1，2，3］，则a［：：－1］＝［3，2，1］。
        前两个冒号表示处理整个列表，也可以写上参数表示处理列表的一部分，
        例如a［2:0:－1］=［3,2］，第一个参数表示起始点包括起始点，第二个参数表示结束点但不包括结束点。
        最后一个参数如果为负的话，需要保证第一个参数大于第二个参数，表示依次递减逆序，否则会输出空列表。
        最后一个参数为正同理。

        """


        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

    def reverse3(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(`s * x`[::-1]) # 此处的反引号是对数组的字符串处理的一种方式
        return s * r * (r < 2 ** 31)


if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse3(-321)