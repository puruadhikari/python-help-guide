"""
You are tasked with designing a function to analyze badge access logs for a secured room. Each badge access log contains:

The name of the employee who badged in.
The time of access, in a 24-hour format (up to 4 digits, such as "800" or "2250").
Your task is to find employees who badged into the room three or more times within any one-hour period. For each such employee, return:

The employee's name.
The earliest one-hour period where they badged in three or more times, along with the list of times they badged in during that period.
If multiple employees meet the criteria, include each of them in the result. If an employee has multiple overlapping
one-hour periods where they meet the criteria, return only the earliest one for that employee.

NOTE : LOOK FOR get_one_hour_valid_entries IMPLEMENTATION
"""

badge_times = [
    ["Paul", "1355"],
    ["Jennifer", "1910"],
    ["Jose", "835"],
    ["Jose", "830"],
    ["Paul", "1315"],
    ["Chloe", "0"],
    ["Chloe", "1910"],
    ["Jose", "1615"],
    ["Jose", "1640"],
    ["Paul", "1405"],
    ["Jose", "855"],
    ["Jose", "930"],
    ["Jose", "915"],
    ["Jose", "730"],
    ["Jose", "940"],
    ["Jennifer", "1335"],
    ["Jennifer", "730"],
    ["Jose", "1630"],
    ["Jennifer", "5"],
    ["Chloe", "1909"],
    ["Zhang", "1"],
    ["Zhang", "10"],
    ["Zhang", "109"],
    ["Zhang", "110"],
    ["Amos", "1"],
    ["Amos", "2"],
    ["Amos", "400"],
    ["Amos", "500"],
    ["Amos", "503"],
    ["Amos", "504"],
    ["Amos", "601"],
    ["Amos", "602"],
    ["Paul", "1416"]
]

from collections import defaultdict


def get_one_hour_valid_entries(entries):
    result = []
    start = 0
    end = 1

    while end < len(entries):
        if entries[end] - entries[start] <= 60:
            if len(result) == 0:
                result.append(entries[start])
            result.append(entries[end])
        else:
            start = end
            if len(result) >= 3:
                return result
            result = []
        end += 1

    return result


def badge_access_logs(badge_times):
    employee_entries = defaultdict(list)
    for emp, bge_time in badge_times:
        employee_entries[emp].append(int(bge_time))
    for key, value in employee_entries.items():
        value.sort()
        employee_entries[key] = value
    output = {}
    for key, values in employee_entries.items():
        if len(get_one_hour_valid_entries(values)) >= 3:
            output[key] = get_one_hour_valid_entries(values)
    return output



print(badge_access_logs(badge_times))