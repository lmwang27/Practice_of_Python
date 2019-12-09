"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

Example
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
Example 2:

Input: "race a car"
Output: false
Explanation: "raceacar"
Challenge
O(n) time without extra memory.

"""


class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def is_palindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1

            end -= 1
        return True

    def is_palindrome2(self, s):
        if s is None or len(s) == 0:
            return True
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s.lower():
                return False
            start += 1
            end -= 1

        return True
