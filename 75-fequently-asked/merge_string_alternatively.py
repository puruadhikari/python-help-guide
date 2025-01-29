"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
"""

def merge_string_alternatively(s,t):
    first = len(s)
    second = len(t)
    counter = 0
    result = []
    while counter < first and counter < second:
        result.append(s[counter])
        result.append(t[counter])
        counter += 1

    if counter < first:
        for i in range(counter,first):
            result.append(s[i])

    if counter < second:
        for j in range(counter,second):
            result.append(t[j])

    return "".join(result)

word1 = "abcdef"
word2 = "pqr"

print(merge_string_alternatively(word1,word2))
