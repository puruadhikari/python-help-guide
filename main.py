from collections import defaultdict
import pandas as pd


# Step 1: Function to build the transition graph from logs
def build_transition_graph(logs):
    # Organize logs by user
    user_logs = defaultdict(list)
    for timestamp, user, resource in logs:
        user_logs[user].append((int(timestamp), resource))

    # Sort each user's logs by timestamp to maintain chronological order
    for user in user_logs:
        user_logs[user].sort()

    # Initialize structures to count transitions and starting states
    transitions = defaultdict(list)
    start_counts = defaultdict(int)  # Count of how many times each resource is the first visited

    # Explicitly initialize nested defaultdict without lambda
    def nested_defaultdict():
        return defaultdict(int)

    next_step_counts = defaultdict(nested_defaultdict)  # Counts of transitions between resources

    # Process each user's logs to calculate transitions
    for user, log_entries in user_logs.items():
        if log_entries:
            # Mark the first resource visited as a transition from _START_
            first_resource = log_entries[0][1]
            start_counts[first_resource] += 1

            # Record transitions between resources for the user
            for i in range(len(log_entries) - 1):
                current_resource = log_entries[i][1]
                next_resource = log_entries[i + 1][1]
                next_step_counts[current_resource][next_resource] += 1

            # Mark the last resource as transitioning to _END_
            last_resource = log_entries[-1][1]
            next_step_counts[last_resource]["_END_"] += 1

    # Compute probabilities for _START_ transitions
    total_starts = sum(start_counts.values())
    transitions["_START_"] = [
        (resource, count / total_starts) for resource, count in start_counts.items()
    ]

    # Compute probabilities for transitions from other resources
    for resource, next_steps in next_step_counts.items():
        total_transitions = sum(next_steps.values())
        transitions[resource] = [
            (next_resource, count / total_transitions)
            for next_resource, count in next_steps.items()
        ]

    return transitions


# Step 2: Convert transition graph to a DataFrame for visualization
def convert_to_dataframe(transition_graph):
    data = []
    for resource, transitions in transition_graph.items():
        for next_resource, probability in transitions:
            data.append({"Resource": resource, "Next Resource": next_resource, "Probability": probability})
    return pd.DataFrame(data)


# Sample logs input
logs = [
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

# Step 3: Build the transition graph
transition_graph = build_transition_graph(logs)

print(transition_graph)

dict({'_START_': [('resource_3', 0.5), ('resource_1', 0.25), ('resource_2', 0.125), ('resource_6', 0.125)],
      'resource_3': [('resource_3', 0.2), ('resource_1', 0.2), ('resource_2', 0.2), ('_END_', 0.4)],
      'resource_1': [('_END_', 0.6666666666666666), ('resource_6', 0.3333333333333333)],
      'resource_2': [('_END_', 1.0)],
      'resource_6': [('resource_5', 0.5), ('_END_', 0.5)],
      'resource_5': [('resource_4', 1.0)],
      'resource_4': [('_END_', 1.0)]})
