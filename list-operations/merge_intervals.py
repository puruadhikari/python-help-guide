"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0], reverse=False)
    merged = []

    for items in intervals:
        if len(merged) == 0:
            merged.append(items)

        if merged[-1][1] >= items[0]:
            merged[-1][1] = items[1]
        else:
            merged.append(items)

    return merged


intervals_data = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(merge(intervals_data))
