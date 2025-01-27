"""
Find the next greater element for each element in an array. Output -1 if the greater element doesn’t exist.
Example:
Input: nums = [2, 1, 2, 4, 3]
Output: [4, 2, 4, -1, -1]
"""
nums = [2, 1, 2, 4, 3]
result = [-1] * len(nums)
stack = []

for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        index = stack.pop()
        result[index] = nums[i]
    stack.append(i)

print(result)