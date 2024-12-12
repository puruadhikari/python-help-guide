"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""
from itertools import combinations
from collections import Counter


def is_valid_list(list_item):
    original_dict = Counter(nums)
    doc_count = Counter(list_item)

    for doc_items in doc_count:
        if doc_count[doc_items] > original_dict[doc_items]:
            return False

    return True


nums = [-1, 0, 1, 2, -1, -4]
sum_dict = {}
cobmi = combinations(nums, 2)
dict_count = Counter(nums)

for items in cobmi:
    if items[0] != items[1]:
        sum_dict[sum(items)] = items

# print(sum_dict)
result = []

for items in nums:
    negative_item = -1 * (items)
    if negative_item in sum_dict:
        sum_list = list(sum_dict[negative_item])
        sum_list.append(items)
        sum_list.sort()
        if is_valid_list(sum_list):
            result.append(sum_list)

result_set = set()

for numbers in result:
    result_set.add(tuple(numbers))

final_result = list(result_set)

print(final_result)