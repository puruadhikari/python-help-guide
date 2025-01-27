"""
You are given an unsorted log file of accesses to web resources for a single day.
Each log entry is a tuple of the form: [<timestamp_in_seconds>, <user_id>, <resource_id>]

timestamp_in_seconds: An integer representing the time of access (in seconds) since 00:00:00 of the same day.
user_id: A string that uniquely identifies a user.
resource_id: A string that uniquely identifies a resource.

User Min/Max Timestamps
Write a function that, given the list of logs, returns a mapping of each user to their earliest (minimum) and latest (maximum) access timestamps.

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

{
  "user_1": [54001, 58523],
  "user_2": [54060, 62314],
  "user_3": [53760, 53760],
  "user_4": [58522, 58522],
  "user_5": [53651, 53651],
  "user_6": [2, 215],
  "user_7": [400, 400],
  "user_8": [100, 100]
}

"""
from collections import defaultdict

def get_user_min_max_timestamps(logs):

    result = defaultdict(list)

    for time, user, resource in logs:
        result[user].append(int(time))

    for key, values in result.items():
        values.sort()
        if len(values) == 1:
            result[key].append(values[0])

        if len(values) > 2:
            result[key] = [values[0], values[-1]]

    return result

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

print(get_user_min_max_timestamps(logs1))