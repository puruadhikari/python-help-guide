"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements
 without changing the order of the remaining elements.
 Input: arr = ["un","iq","ue"]
Output: 4
"""


def max_length(arr):
    unique_strings = []

    for items in arr:
        if len(items) == len(set(items)):
            unique_strings.append(items)
    combinations = [""]
    max_val = 0

    for s in unique_strings:
        for combination in combinations.copy():
            new_combination = combination+s
            if len(new_combination) == len(set(new_combination)):
                combinations.append(new_combination)
                max_val = max(max_val,len(new_combination))
    return max_val

arr_list = ["un","iq","ue","pp"]

print(max_length(arr_list))