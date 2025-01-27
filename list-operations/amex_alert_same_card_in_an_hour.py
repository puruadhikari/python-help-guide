"""
Leetcode - 1604
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period,
while "22:51" - "23:52" is not considered to be within a one-hour period.
Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
"""

from collections import defaultdict

keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]

def get_three_entries_in_hour(a_list):
    i = 0
    j = 3

    while j <= len(a_list):
        temp = a_list[i:j]
        if temp[0] + 60 >= temp[2]:
            return temp
        i += 1
        j += 1

    return []

def same_card_alert(keyName,keyTime):
    global val
    for index in range(len(keyTime)):
        temp = keyTime[index].split(":")
        keyTime[index] = int(temp[0]) * 60 + int(temp[1])
    dict_val = defaultdict(list)
    for i in range(len(keyName)):
        dict_val[keyName[i]].append(keyTime[i])
    for key, val in dict_val.items():
        val.sort()
        dict_val[key] = val
    output = []
    for key,val in dict_val.items():
        if len(get_three_entries_in_hour(val)):
            output.append(key)
    return output


print(same_card_alert(keyName,keyTime))