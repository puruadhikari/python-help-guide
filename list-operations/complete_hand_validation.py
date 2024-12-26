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

    nums = Counter(input_string)
    has_pair = False

    for count in nums.values():
        # Check for a pair
        if count % 3 == 2:  # Leaves a remainder of 2 when divided by 3
            if has_pair:
                return False  # More than one pair is invalid
            has_pair = True
            count -= 2  # Remove the pair

        # Check if the remaining count is divisible by 3
        if count % 3 != 0:
            return False

    # There must be exactly one pair
    return has_pair

print(complete_hand_validation("7777777788"))