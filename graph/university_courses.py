"""
Students may decide to take different "tracks" or sequences of courses in
the Computer Science curriculum. There may be more than one track that includes
the same course, but each student follows a single linear track from a "root"
node to a "leaf" node. In the graph below, their path always moves left to right.

Write a function that takes a list of (source, destination) pairs,
and returns the name of all of the courses that the students could be
taking when they are halfway through their track of courses.

Sample input:
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

Sample output (in any order):
          ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]

All paths through the curriculum (midpoint *highlighted*):

*Intro to C.S.* -> Graphics
Intro to C.S. -> *Data Structures* -> Algorithms -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> Compiler
Creative Writing -> *Databases* -> System Administration
*Creative Writing* -> System Administration
Creative Writing -> *Data Structures* -> Algorithms -> COBOL
Creative Writing -> *Data Structures* -> Logic -> COBOL
Creative Writing -> *Data Structures* -> Logic -> Compilers
"""

from collections import defaultdict


def find_midpoint_courses(all_courses):
    # Step 1: Build the directed graph (adjacency list)
    graph = defaultdict(list)
    in_degree = defaultdict(int)  # To track incoming edges for root node detection

    for src, dest in all_courses:
        graph[src].append(dest)
        in_degree[dest] += 1  # Count incoming edges
        if src not in in_degree:  # Ensure src is in the dictionary
            in_degree[src] = 0

    # Step 2: Find root nodes (courses with no incoming edges)
    roots = [node for node in in_degree if in_degree[node] == 0]

    # Step 3: Perform DFS from each root and find midpoints
    def dfs(course, path):
        path.append(course)

        # If it's a leaf node (no outgoing edges), process the path
        if course not in graph:
            midpoint_idx = len(path) // 2  # Get the midpoint index
            midpoints.add(path[midpoint_idx])
        else:
            for next_course in graph[course]:
                dfs(next_course, path[:])  # Pass a copy of the path to avoid modifying it

    midpoints = set()
    for root in roots:
        dfs(root, [])

    return list(midpoints)


# Test Input
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

# Expected Output: ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]
print(find_midpoint_courses(all_courses))
