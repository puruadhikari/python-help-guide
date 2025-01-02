"""
You are given two arrays of integers nums1 and nums2, possibly of different lengths.
The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6,
inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2.
Return -1 if it is not possible to make the sum of the two arrays equal.



Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
"""


def min_operations(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    operations = 0
    sum1, sum2 = sum(nums1), sum(nums2)
    if sum1 > sum2:
        nums1, nums2 = nums2, nums1
        sum1, sum2 = sum2, sum1

    difference = sum2 - sum1
    gains = []
    for num1 in nums1:
        gains.append(6 - num1)
    for num2 in nums2:
        gains.append(num2 - 1)

    gains.sort(reverse=True)

    for gain in gains:
        difference -= gain
        operations += 1
        if difference <= 0:
            return operations

    return -1


nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,2,2]

print(min_operations(nums1,nums2))