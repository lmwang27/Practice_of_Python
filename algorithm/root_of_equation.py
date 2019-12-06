"""
Given an equation: ax2 + bx + c = 0. Find the root of the equation.

If there are two roots, return a list with two roots in it.
If there are only one root, return a list with only one root in it.
If there are no root for the given equation, return an empty list.

Example
Example 1:

Input: a = 1, b = -2, c = 1
Output: [1]
Explanation:
The equation has a root and returns to [1].
Example 2:

Input: a = 1, b = -3, c = 2
Output: [1,2]
Explanation:
The equation has two roots, returning [1,2] and the first number should be small

"""
import math


class Solution:
    """
    # @param {double} a, a decimal
    # @param {double} b, a decimal
    # @param {double} c, a decimal
    # @return {double[]} a float array
    """


def root_of_equation(self, a, b , c):
    if b * b - 4 * a * c < 0:
        return []
    if b * b - 4 * a * c == 0:
        return [-b * 1.0 /2 /a ]
    if b * b - 4 * a * c > 0 :
        delta = math.sqrt(b * b - 4 * a * c)
        return sorted([(-b-delta)/(2 * a), (-b + delta)/(2 * a)])
