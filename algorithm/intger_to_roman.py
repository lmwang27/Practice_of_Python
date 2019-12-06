"""
Description
中文
English
Given an integer, convert it to a roman numeral.

The number is guaranteed to be within the range from 1 to 3999.
Example

Example 1:

Input: 1
Output: "I"
Example 2:

Input: 99
Output: "XCIX"

Clarification
What is Roman Numeral?

https://en.wikipedia.org/wiki/Roman_numerals
https://zh.wikipedia.org/wiki/罗马数字
http://baike.baidu.com/view/42061.htm

"""


class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def int__to_roman(self, n):
        # write your code here
        m_m = ["", "M", "MM", "MMM"]
        c_c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x_x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i_i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return m_m[n // 1000] + c_c[(n % 1000)//100] + x_x[(n % 100)//10] + i_i[n % 10]


if __name__ == '__main__':
    test = Solution()
    print(test.int__to_roman(99))
