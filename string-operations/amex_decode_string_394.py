"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
 etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_stack = []
        string_stack = []

        current_string = ""
        current_count = 0

        for char in s:
            if char.isdigit():
                current_count = int(current_count) * 10 + int(char)
            elif char == "[":
                count_stack.append(current_count)
                string_stack.append(current_string)
                current_string = ""
                current_count = 0
            elif char == "]":
                number = count_stack.pop()
                prev_string = string_stack.pop()
                current_string = prev_string + current_string * number
            else:
                current_string += char

        return current_string

sol = Solution()

print(sol.decodeString("3[a]2[bc]"))