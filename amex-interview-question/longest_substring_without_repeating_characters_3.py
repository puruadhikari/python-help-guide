"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    s_list = list(s)

    end = 0
    counter = 0
    check_set = set()
    max_value = 0

    while end < len(s_list):
        if s_list[end] not in check_set:
            counter += 1
            max_value = max(counter, max_value)
            check_set.add(s_list[end])
            end += 1
        else:
            counter = 0
            check_set.clear()

    return max_value

print(length_of_longest_substring("abcabcbb"))