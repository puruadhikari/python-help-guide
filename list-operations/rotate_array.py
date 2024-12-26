"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
"""

from collections import deque


def rotate_list(nums, k):
    queue = deque(nums)

    for i in range(k):
        temp = queue.pop()
        queue.appendleft(temp)

    for j in range(len(nums)):
        nums[j] = queue[j]

    return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate_list(nums,k))