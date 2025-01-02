"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

NOTE : Not the best solution as it is O(n3)
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0

        for outer in range(len(nums) + 1):
            for inner in range(outer + 1, len(nums) + 1):
                if k == sum(nums[outer:inner]):
                    counter += 1

        return counter
