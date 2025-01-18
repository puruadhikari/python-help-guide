"""
Minimum Deletions to Make Character Frequencies Unique
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
s = "aaabbbccc" output=3
"""
def number_of_char_delete(s):
    from collections import Counter

    s_counter = Counter(s)
    has_value = set()
    number_of_deletes = 0

    for key, value in s_counter.items():
        while value > 0 and value in has_value:
            value -= 1
            number_of_deletes += 1
        has_value.add(value)

    return number_of_deletes

s = "aaabbbccc"
print(number_of_char_delete(s))