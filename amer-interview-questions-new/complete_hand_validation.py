"""
Question 1: Complete Hand Validation Write a function that determines whether a string of digits (0-9) represents a "complete hand." A "complete hand" satisfies the following conditions:

It contains exactly one pair (two of the same digit).
All other digits form groups of three (triples).
Input:

A string hand containing digits (0-9).
Output:

Return True if the string represents a complete hand; otherwise, return False.
Examples:

Input: "11333666" → Output: True (pair of 1's, triples of 3's and 6's)
Input: "77777777" → Output: True (pair of 7's, remaining 7's form triples)
Input: "5566999" → Output: False (no valid pair, multiple pairs exist)
Input: "678999" → Output: False (no pairs present)
Input: "22" → Output: True (pair of 2's)

"""
from collections import Counter


def complete_hand_validation(input_string):
    nums = Counter(input_string)
    pair_count = 0
    valid_values = {2, 3}

    for item in nums.values():
        if item == 2:
            pair_count += 1

        if pair_count > 1:
            return False

        if item not in valid_values:
            return False

    return True

print(complete_hand_validation("678999"))