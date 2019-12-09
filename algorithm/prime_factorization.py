"""
Description
中文
English
Prime factorize a given integer.

Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]

"""
import math


class Solution:
    def prime_factorization(self, num):
        res = []

        up = int(math.sqrt(num)) + 1

        for i in range(2, up):
            while num % i == 0:
                num = num // i
                res.append(i)

        if num != 1:
            res.append(num)

        return res
