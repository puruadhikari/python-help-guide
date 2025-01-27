"""
You are given:

A list of candidate words (e.g. ["cat", "baby", "dog", "bird", "car", "ax"]).
A test string (e.g. "teabnihis").

Determine if at least one of the candidate words can be formed using the letters from the test string.
Forming a word means each letter in the word must appear in the test string at least as many times as it appears
in the word (i.e., you can’t reuse letters more times than they appear in the test string).
If multiple words can be formed, any valid one can be returned. If no candidate word can be formed,
return None or an equivalent.
words = ["cat", "baby", "dog", "bird", "car", "ax"]
string2 = "tecanihis"
return "cat"
"""
from collections import Counter

words = ["cat", "baby", "dog", "bird", "car", "ax"]
string2 = "tecanihis"

def find_embedded_word(words, test_str):
    string_dict = Counter(test_str)

    for word in words:
        can_be_formed = True
        word_counter = Counter(word)

        for char, count in word_counter.items():
            if char not in string_dict or count > string_dict[char]:
                print(f"{word} cannot be formed using {test_str}")
                can_be_formed = False
                break

        if can_be_formed:
            return word

    return None

print(find_embedded_word(words,string2))