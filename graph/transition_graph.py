"""
You are tasked with analyzing website clickstream logs to build a transition graph that represents user navigation between resources. The graph should include the _START_ state, which represents the first resource a user visits, and the _END_ state, which represents the termination of a user's session. Each resource should have a list of possible next steps along with their probabilities. The _END_ state itself is a terminal state and should not appear as a starting resource.
Input:
Logs: A list of tuples, where each tuple consists of:
A timestamp (str) in milliseconds,
A user ID (str),
A resource (str) representing a visited page.
Output:
An adjacency list (dictionary) where:
Each key is a resource or _START_.
Each value is a list of tuples containing the possible next resources and their probabilities.

Output:
An adjacency list (dictionary) where:
Each key is a resource or _START_.
Each value is a list of tuples containing the possible next resources and their probabilities.

{
    "_START_": [["resource_3", 0.5], ["resource_2", 0.125], ["resource_1", 0.25], ["resource_6", 0.125]],
    "resource_1": [["_END_", 0.6666667], ["resource_6", 0.33333334]],
    "resource_2": [["_END_", 1.0]],
    "resource_3": [["_END_", 0.4], ["resource_3", 0.2], ["resource_2", 0.2], ["resource_1", 0.2]],
    "resource_4": [["_END_", 1.0]],
    "resource_5": [["resource_4", 1.0]],
    "resource_6": [["__END_", 0.5], ["resource_5", 0.5]],
}
"""

from collections import defaultdict

logs1 = [
    ("6500", "user_1", "resource_1"),
    ("4200", "user_2", "resource_2"),
    ("7800", "user_22", "resource_1"),
    ("980", "user_7", "resource_2"),
    ("23", "user_6", "resource_1"),
    ("6000", "user_1", "resource_3"),
    ("345", "user_6", "resource_5"),
    ("3200", "user_2", "resource_3"),
    ("2", "user_1", "resource_3"),
    ("201", "user_6", "resource_6"),
    ("998", "user_8", "resource_6"),
    ("5621", "user_3", "resource_3"),
    ("10212", "user_6", "resource_4"),
    ("29899", "user_5", "resource_3"),
]

def transition_graph(logs):
    user_logs = defaultdict(list)

    for time, user, resource in logs:
        user_logs[user].append((int(time), resource))

    for items in user_logs:
        user_logs[items].sort()

    start_count = defaultdict(int)
    next_step = defaultdict(lambda: defaultdict(int))

    for user, log_entries in user_logs.items():
        if log_entries:
            first_resource = log_entries[0][1]
            start_count[first_resource] += 1

            for i in range(len(log_entries) - 1):
                current_resource = log_entries[i][1]
                next_resource = log_entries[i + 1][1]
                next_step[current_resource][next_resource] += 1

        last_entry = log_entries[-1][1]
        next_step[last_entry]["_END_"] += 1

    transitions = defaultdict(list)

    total_starts = sum(start_count.values())
    transitions["_START_"] = [(resource, count / total_starts) for resource, count in start_count.items()]

    for resource, next_steps_items in next_step.items():
        total_transitions = sum(next_steps_items.values())
        transitions[resource] = [
            (next_resource, count / total_transitions)
            for next_resource, count in next_steps_items.items()
        ]

    return transitions

print(transition_graph(logs=logs1))