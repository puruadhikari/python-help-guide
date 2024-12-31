"""
You are given an unsorted log file of accesses to web resources for a single day.
Each log entry is a tuple of the form: [<timestamp_in_seconds>, <user_id>, <resource_id>]

timestamp_in_seconds: An integer representing the time of access (in seconds) since 00:00:00 of the same day.
user_id: A string that uniquely identifies a user.
resource_id: A string that uniquely identifies a resource.

Write a function that, given the list of logs, determines which resource has the highest number of
 accesses in any 5-minute window and returns the resource along with the maximum count in that window.

A 5-minute window means 300 seconds.
If there are ties, you may return any resource with the maximum count (the problem statement
doesn’t require tie-breaking).

Example:
Suppose we have the following logs (simplified for illustration):
logs1 = [    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200",   "user_6", "resource_5"],
    ["215",   "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_4", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2",     "user_6", "resource_1"],
    ["100",   "user_6", "resource_6"],
    ["400",   "user_7", "resource_2"],
    ["100",   "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"]
]
("resource_3", 4)
"""
from collections import defaultdict

logs = [["58523", "user_1", "resource_1"],
        ["62314", "user_2", "resource_2"],
        ["54001", "user_1", "resource_3"],
        ["200", "user_6", "resource_5"],
        ["215", "user_6", "resource_4"],
        ["54060", "user_2", "resource_3"],
        ["53760", "user_3", "resource_3"],
        ["58522", "user_4", "resource_1"],
        ["53651", "user_5", "resource_3"],
        ["2", "user_6", "resource_1"],
        ["100", "user_6", "resource_6"],
        ["400", "user_7", "resource_2"],
        ["100", "user_8", "resource_6"],
        ["54359", "user_1", "resource_3"]
        ]


def count_five_minutes(time_list):
    counter = 0
    if len(time_list) == 1:
        return 0

    for index in range(1, len(time_list)):
        if time_list[index] - time_list[index - 1] <= 300:
            # print(time_list[index],time_list[index-1],time_list[index]-time_list[index-1])
            counter += 1

    return counter


result = defaultdict(list)

for time, user, resource in logs:
    result[resource].append(int(time))

output = []

for key, values in result.items():
    values.sort()
    result[key] = values

for key, values in result.items():
    five_min_counter = count_five_minutes(values)
    output.append((key, five_min_counter))

output.sort(key=lambda x: x[1], reverse=True)

print(output[0])