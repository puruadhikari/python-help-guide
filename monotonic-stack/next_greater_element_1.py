"""
The next greater element of some element x in an array is the first greater element that is to the
right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums2)
        stack = []
        result_dict = {}
        output = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                result[index] = nums2[i]
            stack.append(i)
        for idx in range(len(nums2)):
            result_dict[nums2[idx]] = result[idx]

        for j in range(len(nums1)):
            output.append(result_dict[nums1[j]])

        return output