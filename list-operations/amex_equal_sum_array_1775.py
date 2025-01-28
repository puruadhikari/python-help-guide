"""
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2.
Return -1 if it is not possible to make the sum of the two arrays equal.

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
"""

def min_operations(nums1, nums2):
    sum1 = sum(nums1)
    sum2 = sum(nums2)

    if sum1 > sum2:
        sum1,sum2 = sum2,sum1
        nums1,nums2 = nums2,nums1

    difference = sum2-sum1
    gains = []
    operation = 0
    for num1 in nums1:
        gains.append(6-num1)
    for num2 in nums2:
        gains.append(num2-1)

    gains.sort(reverse=True)
    for gain in gains:
        difference -= gain
        operation += 1
        if difference <= 0:
            return operation
    return -1

print(min_operations( [1,2,3,4,5,6],[1,1,2,2,2,2]))