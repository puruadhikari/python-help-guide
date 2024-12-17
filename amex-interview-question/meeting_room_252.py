"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
"""


def meeting_room(intervals):
    intervals.sort(key=lambda x: x[0])
    output = [intervals[0]]

    for index in range(1, len(intervals)):
        last_entry = output[-1]
        if last_entry[1] > intervals[index][0]:
            return False

        return True

intervals = [[7,10],[2,4]]
print(meeting_room(intervals))