"""
Description

Given a string, convert it to an integer.
You may assume the string is a valid integer number that can be presented
by a signed 32bit integer (-231 ~ 231-1).

Example 1:
Input:  "123"
Output: 123

Explanation:
return the Integer.

Example 2:
Input:  "2"
Output: 2
Explanation:
return the Integer.

"""


class Solution:
    def string_integer(self, strr):
        num, sig = 0, 1

        if strr[0] == '-':
            sig = -1
            strr = strr[1:]

        for c in strr:
            num = num*10 + ord(c) - ord('0')

        return num * sig