"""
implement a substitution cipher for encryption using a specific substitution logic:

Example Step-by-Step:
Let's walk through the example provided:

Given String:
"bkmbkw"
Step 1: Extract Unique Alphabets in Order of Appearance
The unique letters, in order, are: b, k, m, w.
Step 2: Map to Alphabetical Order
Alphabetical order is a, b, c, d, so the mapping would be:
'a' -> 'b'
'b' -> 'k'
'c' -> 'm'
'd' -> 'w'
Step 3: Apply the Mapping to Encrypt the String
For each letter in the original string, replace it based on the above mapping while preserving the case.
"""

input_string = "bkmbkw"
char_set = set()
ordered_list = ["a","b","c","d","e","f","g","h"]
mapped_dict = {}

index = 0
decrypted = []

for item in list(input_string):
    if item not in char_set:
        char_set.add(item)
        mapped_dict[item] = ordered_list[index]
        index += 1

for char_item in list(input_string):
    decrypted.append(mapped_dict[char_item])

print("".join(decrypted))
