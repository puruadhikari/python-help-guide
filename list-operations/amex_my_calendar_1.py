"""
You are implementing a program to use as your calendar.
We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a
booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully
without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
"""

bookings = ["MyCalendar", "book", "book", "book"]
times = [[], [10, 20], [15, 25], [20, 30]]

output = []
result = []

for index, booking in enumerate(bookings):
    if booking == "MyCalendar":
        output.append(None)
    else:
        if len(result) == 0:
            output.append(True)
            result.append(times[index])
        else:
            start, end = result[-1][0], result[-1][1]

            if end > times[index][0]:
                length = len(result)
                result[length - 1] = [min(start, times[index][0]), max(end, times[index][1])]
                output.append(False)
            else:
                result.append(times[index])
                output.append(True)

print(output)
