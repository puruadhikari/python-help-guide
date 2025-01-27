"""
At a university, every course has at most one prerequisite that must be taken first.
No two courses share the same prerequisite, and there is exactly one unique path through the program of study.

Given a list of (prerequisite, course) pairs, determine the course that is in the middle of the program.
If the program has an even number of courses, return the first course of the two middle courses.

pairs1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]
Software Design → Computer Networks → Computer Architecture → Data Structures → Algorithms → Foundations of Computer Science → Operating Systems
output "Data Structures"

"""

from collections import defaultdict

pairs1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]


def is_middle(courses):
    graph = defaultdict(str)
    path = defaultdict(str)

    for pre, course in courses:
        graph[course] = pre
        path[pre] = course

    for key, value in graph.items():
        if value not in graph:
            start = value

    result = [start]

    while start:
        if path[start] != '':
            result.append(path[start])
        start = path[start]

    if len(result) % 2 == 0:
        return [result[(len(result) // 2) - 1], result[(len(result) // 2)]]
    else:
        return [result[(len(result) // 2)]]

    return []


print(is_middle(pairs1))
