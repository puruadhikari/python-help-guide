"""
Question 1: Maximum Number of People in the Mall
Given an array of logs representing people entering and exiting a mall, where each log is in the form [numOfPeople, time, enterOrExit]:

numOfPeople indicates the number of people involved in the event.
time is the timestamp of the event.
enterOrExit is a binary indicator, where 1 means people entered the mall, and 0 means people exited.
logs = [
    [12, "10:00", 1],  # 12 people entered at 10:00
    [5, "10:15", 0],   # 5 people exited at 10:15
    [7, "10:30", 1],   # 7 people entered at 10:30
    [3, "10:45", 0],   # 3 people exited at 10:45
    [8, "11:00", 1],   # 8 people entered at 11:00
    [10, "11:15", 0]   # 10 people exited at 11:15
]
The maximum number of people was 19 at 11:00.
"""

logs = [
    [12, "10:00", 1],  # 12 people entered at 10:00
    [5, "10:15", 0],  # 5 people exited at 10:15
    [7, "10:30", 1],  # 7 people entered at 10:30
    [3, "10:45", 0],  # 3 people exited at 10:45
    [8, "11:00", 1],  # 8 people entered at 11:00
    [10, "11:15", 0]  # 10 people exited at 11:15
]
number_of_people = 0
temp_count = 0
a_dict = []

for log in logs:
    count = log[0]
    log_time = log[1]
    in_out = log[2]

    if in_out == 1:
        temp_count += count
    elif in_out == 0:
        temp_count -= count

    number_of_people = max(temp_count, number_of_people)

print(f"max number of people at any given time is : {number_of_people}")