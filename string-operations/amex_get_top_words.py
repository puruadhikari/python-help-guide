"""
You are tasked with processing a string containing (word, count) pairs. Your goal is to extract the top words
 and their counts, sorted in descending order by their counts, subject to the following conditions:

Only include words whose lengths are greater than or equal to a given minWordLength.
Limit the output to at most wordLimit words.

nput:

A string s containing (word, count) pairs separated by commas, where:
word is a string representing a word.
count is an integer representing the count for that word.
An integer wordLimit indicating the maximum number of words to return.
An integer minWordLength specifying the minimum length a word must have to be included in the output.
Output:

A list of tuples (word, count) representing the top words and their counts, sorted in descending order by count.
If multiple words have the same count, they should appear in the order they are encountered in the input string.

s = "abc,500 sadhasibkedsak,230239203 fsgdfssd,78 sss,56 ss,56 sss,5678 sssdsds,56 ssssdsd,56"
wordLimit = 3
minWordLength = 3

s1 = "apple,300 banana,400 apple,500 cherry,200"
"""
from collections import defaultdict

#s1 = "abc,500 sadhasibkedsak,230239203 fsgdfssd,78 sss,56 ss,56 sss,5678 sssdsds,56 ssssdsd,56"
s1 = "apple,300 banana,400 apple,500 cherry,200"
wordLimit1 = 3
minWordLength1 = 5


def get_top_words(s, wordLimit, minWordLength):
    s_list = s.split(" ")
    fruit_dict = defaultdict(list)

    for items in s_list:
        item = items.split(",")
        fruit = item[0]
        count = int(item[1])

        fruit_dict[fruit].append(count)

    result = {}

    for name, value in fruit_dict.items():
        if len(name) >= minWordLength and max(value) > wordLimit:
            result[name] = max(value)

    return result


print(get_top_words(s1, wordLimit1, minWordLength1))
