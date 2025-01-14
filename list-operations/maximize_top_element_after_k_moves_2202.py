"""
You are given a 0-indexed integer array nums representing the contents of a pile,
where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile.
This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves.
In case it is not possible to obtain a non-empty pile after k moves, return -1.

Example 1:

Input: nums = [5,2,2,4,0,6], k = 4
Output: 5
Explanation:
One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
"""

from collections import deque

def maximum_top(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    queue = deque()
    if not nums or len(nums) <= 1:
        return -1

    for num in nums:
        queue.append(num)

    top_item = queue.popleft()

    for item in range(k - 2):
        top_item = max(top_item, queue.popleft())

    return top_item

nums = [5,2,2,4,0,6]
k = 4

print(maximum_top(nums,4))