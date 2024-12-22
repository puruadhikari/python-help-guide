"""
THIS IS NOT PRODUCING THE CORRECT RESULT
"""

from collections import defaultdict

endings = [5, 10]
choices = [(3, 7, 9), (9, 10, 8)]


def count_page_endings(endings, choices):
    graph = defaultdict(list)
    for page, source, destination in choices:
        graph[page].append(source)
        graph[page].append(destination)

    page_counter = defaultdict(int)
    visited = set()
    print(graph)

    def dfs(page, visited):

        page_counter[page] += 1

        visited.add(page)

        if page not in graph:
            page ==1

        if page in endings:
            return

        for next_page in graph[page]:
            if next_page not in visited:
                dfs(next_page, visited)

    dfs(1, visited)

    return page_counter


print(count_page_endings(endings, choices))