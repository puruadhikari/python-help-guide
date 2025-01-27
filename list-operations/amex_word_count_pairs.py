"""
You are given a list of strings where each string represents a (word, count) pair. Each word is a string,
and the count is an integer representing its frequency. Write a function getTopWords that accepts this list,
along with two additional parameters: wordLimit and minWordLength. The function should return the top words
sorted in descending order by their count, limited by the wordLimit

s = [
    "apple, 150",
    "banana, 200",
    "strawberry, 120",
    "grape, 95",
    "kiwi, 50",
    "watermelon, 300",
    "pear, 80",
    "blueberry, 220",
    "orange, 175",
    "peach, 60",
    "fig, 40"
]

wordLimit = 5
minWordLength = 5

Output
[
"watermelon, 300",
"blueberry, 220",
"banana, 200",
"orange, 175",
"apple, 150"
]

"""
wordLimit = 5
s_list = [
    "apple, 150",
    "banana, 200",
    "strawberry, 120",
    "grape, 95",
    "kiwi, 50",
    "watermelon, 300",
    "pear, 80",
    "blueberry, 220",
    "orange, 175",
    "peach, 60",
    "fig, 40"
]
output = []
for items in s_list:
    fruit, count = items.split(",")
    if len(fruit) >= wordLimit:
        output.append((fruit, int(count)))

output.sort(key=lambda x: x[1],reverse=True)

result = []

for values in output[:5]:
    string_result = values[0] + "," + str(values[1])
    result.append(string_result)

print(result)