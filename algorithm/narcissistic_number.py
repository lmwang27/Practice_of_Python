"""
Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits. See wiki

For example the 3-digit decimal number 153 is a narcissistic number because 153 = 13 + 53 + 33.

And the 4-digit decimal number 1634 is a narcissistic number because 1634 = 14 + 64 + 34 + 44.

Example 1:

Input: 1
Output: [0,1,2,3,4,5,6,7,8,9]
Example 2:

Input:  2
Output: []
Explanation: There is no Narcissistic Number with 2 digits.


"""


def is_narcissistic(num, n):
    res = 0
    temp = num
    while num != 0:
        res += (num % 10) ** n
        print(res, num%10)
        num = num//10
        print(num)

    print(res,num)
    return res == temp

class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """

    def get_narcissistic_numbers(self, n):
        # write your code here

        # return list
        results = []

        # calculate the range of numbers to process
        start = 10 ** (n-1)
        print(start)
        end = 10 ** n
        print(end)

        if n == 1:
            results.append(0)

        for i in range(start, end):
            if is_narcissistic(i, n):
                results.append(i)

        return results


if __name__ == "__main__":
    n = 1
    test = Solution()
    print(test.get_narcissistic_numbers(n))

