from collections import defaultdict

courses = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]


# courses = [[0,1]]

def can_finish(courses, numCourses):
    graph = {i: [] for i in range(numCourses)}

    for crs, pre in courses:
        graph[crs].append(pre)

    visited = set()
    print(graph)

    def dfs(course):
        if course in visited:
            return False

        if course not in graph:
            return True

        visited.add(course)

        for sub_course in graph[course]:
            if not dfs(sub_course):
                return False

        visited.remove(course)

        return True

    for crs in graph:
        if not dfs(crs):
            return False

    return True


print(can_finish(courses, 5))