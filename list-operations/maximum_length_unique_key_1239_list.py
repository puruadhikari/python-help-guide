"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no
elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4 .
"""

arr_1 = ["un", "iq", "ue"]


def count_max_length(arr):
    if len(arr) == 1:
        return len(arr[0])

    a_dict = {}

    for item in arr:
        a_dict[item] = set(list(item))

    print(a_dict)
    max_length = 0

    for outer in range(len(arr)):
        for inner in range(outer + 1, len(arr)):
            result = len(a_dict[arr[outer]].intersection(a_dict[arr[inner]]))

            if result == 0:
                max_length = max(len(a_dict[arr[outer]]) + len(a_dict[arr[inner]]), max_length)

    return max_length


print(count_max_length(arr_1))
