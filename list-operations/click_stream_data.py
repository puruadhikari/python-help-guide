"""
You have access to anonymized clickstream data collected from a client's website.
Each user's browsing history is a chronological sequence of unique URLs they visited.
Your task is to write a function findLongestHistory(userA, userB) that finds the longest contiguous sequence of
URLs that appears in both users' browsing histories.

Input:
userA: A list of strings representing the first user's browsing history in chronological order.
userB: A list of strings representing the second user's browsing history in chronological order.

Output:
A list of strings representing the longest contiguous sequence of URLs shared between the two users.
If no common sequence exists, return an empty list.

userA = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
userB = ["/start", "/pink", "/register", "/orange", "/red", "a"]

findLongestHistory(userA, userB)

["/pink", "/register", "/orange"]
"""
userA = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
userB = ["/start", "/pink", "/register", "/orange", "/red", "a"]
m = len(userA)
n = len(userB)
result = []

for i in range(m):
    k = 0
    result_temp = []
    for j in range(n):
        while i+k < m and j+k < n and userA[i+k] == userB[j+k]:
            result_temp.append(userA[i+k])
            k += 1
        if len(result_temp) > len(result):
            result = result_temp

print(result)