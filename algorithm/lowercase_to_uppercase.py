"""
Convert a lowercase character to uppercase.
Example
Example 1:

Input: 'a'
Output: 'A'
Example 2:

Input: 'b'
Output: 'B'

"""


class Solution:
    def low_to_upper(self, letter):
        return chr(ord(letter)-ord('0')+'A')