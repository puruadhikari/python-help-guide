"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
NOTE : Below solution is O(m+n) not O(log (m+n)).
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

def median_sorted_arrays(nums1,nums2):
    first_length = 0
    second_length = 0
    result = []

    while first_length < len(nums1) and second_length < len(nums2):
        if nums1[first_length] < nums2[second_length]:
            result.append(nums1[first_length])
            first_length += 1
        else:
            result.append(nums2[second_length])
            second_length += 1

    while first_length < len(nums1):
        result.append(nums1[first_length])
        first_length += 1

    while second_length < len(nums2):
        result.append(nums2[second_length])
        second_length += 1

    index = len(result)//2
    if len(result)%2 ==1:
        return result[index]
    else:
        return float((result[index]+result[index-1])/2)

print(median_sorted_arrays([1,2],[3,4]))