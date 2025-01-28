"""
Given an array of meeting time intervals  where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""
def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Extract start and end times into separate lists
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    start_ptr = 0
    end_ptr = 0
    rooms = 0
    max_rooms = 0
    n = len(intervals)

    # Iterate through all the meetings
    while start_ptr < n:
        # If there's an overlap, allocate a new room
        if start_times[start_ptr] < end_times[end_ptr]:
            rooms += 1
            start_ptr += 1
        else:
            # No overlap, free up a room
            rooms -= 1
            end_ptr += 1

        # Update the maximum number of rooms needed
        max_rooms = max(max_rooms, rooms)

    return max_rooms

# Example Usage:
intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))  # Output: 2

# Additional Test Cases
print(minMeetingRooms([[7,10],[2,4]]))  # Output: 1
print(minMeetingRooms([[0,30],[5,10],[15,20],[25,35]]))  # Output: 2
print(minMeetingRooms([[1,5],[2,6],[4,8],[5,7]]))  # Output: 3
print(minMeetingRooms([[0,1]]))  # Output: 1
print(minMeetingRooms([[0,10],[0,10],[0,10]]))  # Output: 3
