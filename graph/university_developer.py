"""
You are tasked with building a system for a university that finds courses shared by pairs of students.
The university provides you with a list of (student ID, course name) pairs representing the courses each
student is enrolled in. Your job is to implement a function that takes this input and returns a mapping for
 every pair of students, listing all the courses they share.

The output should only include pairs of students who share at least one course. If a pair of students does
not share any courses, they should not appear in the result. The order of the pairs does not matter.
{
    (17, 58): ['Linear Algebra', 'Software Design'],
    (58, 94): ['Economics'],
    (25, 58): ['Economics'],
    (25, 94): ['Economics']
}
"""

enrollments = [
    (58, "Linear Algebra"),
    (94, "Art History"),
    (94, "Operating Systems"),
    (17, "Software Design"),
    (58, "Mechanics"),
    (58, "Economics"),
    (17, "Linear Algebra"),
    (17, "Political Science"),
    (94, "Economics"),
    (25, "Economics"),
    (58, "Software Design")
]



from collections import defaultdict
from itertools import combinations


def find_shared_courses(enrollments):
    graph = defaultdict(list)

    for student_id, course in enrollments:
        graph[course].append(student_id)
    result = defaultdict(list)

    for course, ids in graph.items():

        if len(ids) == 2:
            id1 = min(ids)
            id2 = max(ids)
            result[(id1, id2)].append(course)
        if len(ids) > 2:
            groups = combinations(ids, 2)
            for items in groups:
                id1 = min(items)
                id2 = max(items)
                result[(id1, id2)].append(course)

    return result

print(find_shared_courses(enrollments))