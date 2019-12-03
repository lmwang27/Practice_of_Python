class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def is_valid_parentheses(self, s):
        # write your code here
        stack = []
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            elif ch == ']' and (not stack or stack[-1] != '['):
                return False

            elif ch == ')' and (not stack or stack[-1] != '('):
                return False

            elif ch == '}' and (not stack or stack[-1] != '{'):
                return False
            else:
                stack.pop()

        return not stack
