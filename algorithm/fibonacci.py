"""
Description
中文
English
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Example
Example 1:
Input:  1
Output: 0
Explanation:
return the first number in  Fibonacci sequence .

Example 2:
Input:  2
Output: 1
Explanation:
return the second number in  Fibonacci sequence .

"""


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def nth_num_fibonacci(n):
    return fibonacci(n)


def fibonacci2(self, n):
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return a