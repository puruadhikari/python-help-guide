"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

"""

from collections import Counter


class Solution(object):

    def _check_can_form(self, word, char_dict):
        word_counter = Counter(word)
        can_form = False

        for key, value in word_counter.items():
            if key in char_dict and word_counter[key] <= char_dict[key]:
                can_form = True
            else:
                can_form = False
                break

        return can_form

    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_counter = Counter(chars)
        total_count = 0

        for word in words:
            if self._check_can_form(word, chars_counter):
                total_count += len(word)

        return total_count
