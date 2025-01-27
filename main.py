n =3
from collections import deque

queue = deque([("", 0, 0)])  # Start with an empty string and 0 open/close parentheses
result = []

while queue:
    current, open_count, close_count = queue.popleft()

    # If the current string is complete, add it to the result
    if len(current) == 2 * n:
        result.append(current)
        continue

    # Add an opening parenthesis if valid
    if open_count < n:
        queue.append((current + "(", open_count + 1, close_count))

    # Add a closing parenthesis if valid
    if close_count < open_count:
        queue.append((current + ")", open_count, close_count + 1))

print(result)