"""
Implement an upper method to convert all characters in a string to uppercase.

The characters not in alphabet don't need to convert.

Example 1:

Input: str = "abc"
Output: "ABC"
Example 2:

Input: str = "aBc"
Output: "ABC"
Example 3:

Input: str = "abC12"
Output: "ABC12"

"""

def lowercase_to_uppercase_2(self, str):
    if str is None or len(str) == 0:
        return str
    else:
        return str.upper()
