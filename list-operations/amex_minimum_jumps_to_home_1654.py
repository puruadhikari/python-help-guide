"""
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i],
and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home.
If there is no possible sequence of jumps that lands the bug on position x, return -1.

Example 1:
Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
"""
from collections import deque

def minimum_jumps(forbidden, a, b, x):
    forbidden_set = set(forbidden)
    visited = set()
    queue = deque()

    if 0 in forbidden_set:
        return -1
    if x == 0:
        return -1

    queue.append((0,False))
    visited.add((0,False))

    upper_bound = max(forbidden) +a+ b
    steps = 0
    while queue:
        for _ in range(len(queue)):
            pos,last_move_backward = queue.popleft()
            forward = pos + a
            if forward ==x:
                return steps+1
            if forward not in forbidden_set and forward <= upper_bound and (forward,False) not in visited:
                queue.append((forward,False))
                visited.add((forward,False))
            if not last_move_backward:
                backward = pos-b
                if backward == x:
                    return steps+1
                if backward not in forbidden_set and backward >=0 and (backward,True) not in visited:
                    queue.append((backward,True))
                    visited.add((backward,True))
        steps += 1
    return -1

forbidden1 = [14,4,18,1,15]
a1= 3
b1 = 15
x1 = 9

print(minimum_jumps(forbidden1,a1,b1,x1))