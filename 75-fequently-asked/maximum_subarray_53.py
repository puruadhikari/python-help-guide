"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
"""
class Solution(object):
    def max_subarray_brute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        if len(nums) == 1:
            return sum(nums)

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                max_val = max(sum(nums[i:j + 1]), max_val)
        return max_val

sol = Solution()
print(sol.max_subarray_brute_force(nums = [-2,1,-3,4,-1,2,1,-5,4]))