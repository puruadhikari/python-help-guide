"""
You are given an array of integers nums, there is a sliding window of size k which is
moving from the very left of the array to the very right. You can only see the k numbers in the window.
NOTE : Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


from collections import deque

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    start = 0
    end = k
    result = []
    queue = deque()

    for index in range(k):
        queue.append(nums[index])

    while end <= len(nums):
        result.append(max(queue))
        if end < len(nums):
            queue.append(nums[end])
        queue.popleft()
        end += 1

    return result

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
