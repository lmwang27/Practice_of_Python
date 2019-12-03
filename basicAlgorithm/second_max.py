class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """

    def secondMax(self, nums):
        # write your code here
        max_value = max(nums[0], nums[1])
        second_max = min(nums[0], nums[1])

        for i in range(2, len(nums)):
            if nums[i] > max_value:
                second_max = max_value
                max_value = nums[i]
            elif nums[i] > second_max:
                second_max = nums[i]

        return second_max
