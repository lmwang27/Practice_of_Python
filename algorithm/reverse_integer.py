"""
Description
Reverse digits of an integer.
Returns 0 when the reversed integer overflows (signed 32-bit integer).

Example
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321

"""


class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """

    def reverse_integer(self, n):
        # write your code here
        sign = 1
        if n < 0:
            sign = -1
            n = abs(n)
        res = 0

        while n != 0:
            temp = res * 10 + n % 10
            n = n // 10
            if temp // 10 != res:
                res = 0
                break

        print(-(1 << 31), (1 << 31) - 1)
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0

        return res * sign


if __name__ == '__main__':

    n = 1534236469
    test = Solution()
    print(test.reverse_integer(n))
