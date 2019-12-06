"""
Description
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example
Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.

"""


class Solution:
    """
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    # the answer is the count of characters that has even number of appereances.
    # for characters that has odd number of appereances,
    # their appereances minus 1 will make their apperances even.
    # And finally we can put an unused character in the middle of the palindrome
    """

    def longest_palindrome(self,s):
        hash = {}

        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash)
        if remove > 0:
            remove -=1

        return len(s) - remove


if __name__ == "__main__":

    s = "abccccdd"

    test = Solution()
    print(test.longest_palindrome(s))
