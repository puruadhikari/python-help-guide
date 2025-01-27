"""
You are given an array of strings words and a string chars.
A string is considered good if it can be formed by characters from chars (each character can only be used once).
Return the sum of the lengths of all the good strings in words.

words = ["cat", "bt", "hat", "tree"]
chars = "atach"

return : 6 - The strings "cat" and "hat" can be formed using the characters in "atach",
"""

from collections import Counter

words = ["cat", "bt", "hat", "tree"]
chars = "atach"
count = 0
char_dict = Counter(chars)

for word in words:
    can_form = True
    word_dict = Counter(word)

    for char in word_dict:
        if word_dict[char] > char_dict[char]:
            can_form = False
            break

    if can_form:
        print(word)
        count += len(word)

print(count)