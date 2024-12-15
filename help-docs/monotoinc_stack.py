"""
Monotonic Increasing Stack: Keeps elements in ascending order (top of the stack has the largest elements).
As you push new elements, you pop all smaller elements first. This is often used
to find the "next smaller element" or to help with certain range queries.

Monotonic Decreasing Stack: Keeps elements in descending order (top of the stack has the smallest elements).
As you push new elements, you pop all larger elements first. This is commonly used to find the "next greater element."
"""

# Brute force way O(n2) which is not ideal
# find the next highest number output to below should be [7, 8, 5, 6, 6, 8, -1]

nums = [2, 7, 3, 5, 4, 6, 8]

result =  [-1]*len(nums)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] > nums[i]:
            result[i] = nums[j]
            break

print(result)

monotonic_decreasing_result = [-1] * len(nums)
stack = []

for index,num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        top_index = stack.pop()
        monotonic_decreasing_result[top_index] = num
    stack.append(index)

print(monotonic_decreasing_result)

# Monotonic_increasing_result
# All logic remains the same but the less than is >= (equals to conditions like 2=2 etc)

monotonic_increasing_result = [-1] * len(nums)
stack_increasing = []

for index,num in enumerate(nums):
    while stack_increasing and nums[stack_increasing[-1]] >= num:
        top_index = stack_increasing.pop()
        monotonic_increasing_result[top_index] = num
    stack_increasing.append(index)

print(monotonic_increasing_result)
