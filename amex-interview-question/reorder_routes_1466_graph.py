from collections import defaultdict

edges_1 = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]


def min_reversal(edges, start_city):
    graph = defaultdict(list)
    # IMP : Using a default dict to get bidirectional graph
    for start, end in edges:
        graph[start].append((end, True))
        graph[end].append((start, False))

    counter = 0
    visited = set()

    def dfs(city):
        nonlocal counter

        visited.add(city)

        for neighbor, to_be_reversed in graph[city]:
            if neighbor not in visited:
                if to_be_reversed:
                    counter += 1
                dfs(neighbor)

    dfs(start_city)

    return counter


print(min_reversal(edges_1, 0))



