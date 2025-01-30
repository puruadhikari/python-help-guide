"""
Description
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
NOTE: first sort the items based on start time
"""
intervals1 = [[7,10],[2,4]]


def is_meeting_possible(intervals):
    intervals.sort()
    print(intervals)
    result = [intervals[0]]
    for index in range(1, len(intervals)):
        last_item = result[-1]
        last_start = last_item[0]
        last_end = last_item[1]

        if last_end > intervals[index][0]:
            return False
        else:
            result[-1] = intervals[index]

    return True


print(is_meeting_possible(intervals1))