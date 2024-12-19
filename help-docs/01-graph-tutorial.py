"""
Basic DFS Example
What is DFS?
Depth-First Search (DFS) is a way to explore a graph by starting at a node and going as deep as possible
along one path before backtracking and trying another path. It’s like following a single narrow hallway from a
room until you can’t go any further, then returning back and taking a different hallway.

Simple Example:
Imagine you have a graph representing friendships:
   A
  / \
 B   C
  \ /
   D

Node A is connected to B and C.
B is connected to A and D.
C is connected to A and D.
D is connected to B and C.

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

Goal: Perform DFS starting from node 'A'.

How DFS Works:

Start at 'A'.
Mark 'A' as visited.
Look at 'A's neighbors: 'B' and 'C'. Pick one (usually the first in the list). Let’s pick 'B'.
Move to 'B', mark 'B' as visited.
From 'B', its neighbors are 'A' (visited) and 'D' (unvisited). Go to 'D'.
Move to 'D', mark 'D' as visited.
From 'D', its neighbors are 'B' (visited) and 'C' (unvisited). Go to 'C'.
Move to 'C', mark 'C' as visited.
From 'C', neighbors 'A' and 'D' are both visited. We can’t go further, so backtrack.
Back at 'D', no unvisited neighbors left. Backtrack to 'B'.
Back at 'B', no unvisited neighbors left. Backtrack to 'A'.
From 'A', we also had 'C' as a neighbor, but it’s already visited.
We visited all nodes in the order: A -> B -> D -> C.

"""
from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph,start=None):
    # define queue
    queue = deque([start])
    visited = set()
    while queue:
        current = queue.popleft()
        print(current)
        visited.add(current)
        nodes = graph[current]
        for node in nodes:
            if node not in visited:
                queue.append(node)

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "A"),
    ("C", "D"),
    ("C", "A"),
    ("D", "A"),
    ("D", "C")
]

graph = {}

for start, end in edges:
    if start not in graph:
        graph[start] = [end]
    else:
        graph[start].append(end)

# Run the DFS
dfs(graph, "A")

# Run the BFS
bfs(graph,"A")
