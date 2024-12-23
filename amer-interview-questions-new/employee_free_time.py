"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees,
also in sorted order.
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
"""


def employee_free_time(schedule):
    all_times = []

    for items in schedule:
        for item in items:
            all_times.append(item)

    all_times.sort()

    print("all time: ", all_times)
    result = [all_times[0]]

    for i in range(1, len(all_times)):
        last_record = result[-1]
        current_start = all_times[i][0]
        current_end = all_times[i][1]

        if last_record[1] > current_start:
            result.pop()
            result.append([last_record[0], max(current_end,last_record[1])])
        else:
            result.append(all_times[i])

    busy_times = []
    print("result: ", result)
    for items in result:
        start = items[0]
        end = items[1]
        for i in range(start, end):
            busy_times.append([i, i + 1])

    output = []
    print("busy time: ", busy_times)
    for i in range(1, 12):
        if [i, i + 1] not in busy_times:
            output.append([i, i + 1])

    return output


schedule1 = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

print("final: " , employee_free_time(schedule1))
