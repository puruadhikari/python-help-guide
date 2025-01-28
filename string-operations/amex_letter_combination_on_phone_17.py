"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
from itertools import product

class Solution(object):
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        output = []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        groups = [list(digit_to_letters[d]) for d in digits]
        if len(groups) == 1:
            return groups[0]

        group_prod = list(product(*groups))
        for items in group_prod:
            output.append("".join(items))

        return output