"""
Description

Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.

Example
Example 1:

Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
Explanation:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?,
we only care about the part which has no duplicate integers.
Example 2:

Input:
nums = [1,2,3]
Output:
[1,2,3]
3
Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.

"""

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        i, j = 1, len(nums)
        num = nums[0]
        count = 0
        while i < j:
            print(i, nums[:i])
            if nums[i] not in nums[:i]:
                i += 1
            else:
                nums[i], nums[j-1] = nums[j-1], nums[i]
                j -= 1
                count += 1

        return len(nums) - count

    def deduplication2(self, nums):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        result = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1

        return result

    def deduplication3(self, nums):
        # Write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result

    def deduplication4(self, nums):
        if nums is None:
            return 0
        nums2 = set(nums)
        i = 0
        for num in nums2:
            nums[i] = num
            i += 1

        return len(nums2)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 1]
    test = Solution()
    print(test.deduplication4(nums))

