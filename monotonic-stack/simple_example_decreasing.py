"""
Find the next smallest element for each element in an array. Output -1 if the greater element doesn’t exist.
Example:
Input: nums = [2, 1, 2, 4, 3]
Output: [4, 2, 4, -1, -1]
"""
nums = [4, 8, 5, 2, 25]
stack = []
result = [-1]* len(nums)
for i in range(len(nums)-1,-1,-1):
    while stack and stack[-1] >= nums[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]
    stack.append(nums[i])

print(result)