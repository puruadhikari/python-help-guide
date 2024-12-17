"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
"""

nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]

class Solution(object):
    def find_length(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        max_length = 0
        m = len(nums1)
        n = len(nums2)

        for i in range(m):
            k = 0
            for j in range(n):
                while i+k < m and j+k < n and nums1[i+k] == nums2[j+k]:
                    k += 1
                max_length = max(max_length,k)
        return max_length

sol = Solution()
print(sol.find_length(nums1,nums2))