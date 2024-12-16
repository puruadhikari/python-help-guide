prerequisites = [[1, 0]]  # [[0, 1], [1, 2], [2, 3], [3, 1], [4, 2]]

course = {}

for item, value in prerequisites:
    if item not in course:
        course[item] = [value]
    else:
        course[item].append(value)


def dfs(graph, start, visited=None):
    if not visited:
        visited = set()

    visited.add(start)
    print(start)

    for nodes in graph[start]:
        if nodes not in visited and start in graph:
            dfs(graph, nodes, visited)
        else:
            return False


if dfs(course, prerequisites[0][0]):
    print("no cyclic")
else:
    print("cyclic")