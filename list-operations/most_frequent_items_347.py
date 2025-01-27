"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        cntr = Counter(nums)
        tuple_list = []
        output = []
        for key,value in cntr.items():
            tuple_list.append((key,value))

        tuple_list.sort(key=lambda x:x[1],reverse = True)

        for key,value in tuple_list[:k]:
            output.append(key)

        return output