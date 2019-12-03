class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        result = []
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append("fizz buzz")
            elif i % 3 == 0:
                result.append("fizz")
            elif i % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(i))

        return result
