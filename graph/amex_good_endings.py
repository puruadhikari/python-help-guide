"""
You are reading a book where the story progresses based on the choices you make.
Each page may lead you to a good ending or a bad ending. Your goal is to figure out
which good endings are actually reachable, given the choices in the book.

Good endings: Pages where the story ends positively.
Bad endings: Pages where the story ends negatively.
Choices: A list of decisions at specific pages that dictate where the story branches.

Inputs:
good_endings: A list of pages where the story ends positively.
Example: [10, 15, 25, 34]

bad_endings: A list of pages where the story ends negatively.
Example: [21, 30, 40]

choices: A list of lists where each entry represents a page with choices and the possible pages you can move to.
Example: choices = [[3, 16, 24], [16, 17, 21], [24, 25, 30]]

This means:
From page 3, you can go to pages 16 or 24.
From page 16, you can go to pages 17 or 21.
From page 24, you can go to pages 25 or 30.

good_endings = [10, 15, 25, 34]
bad_endings = [21, 30, 40]
choices = [[3, 16, 24], [16, 17, 21], [24, 25, 30]]

(Starting Page: 1)
1 → 2 → 3 (Choices: [16, 24])
      16 → 17 (Leads to: No ending)
         → 21 (Bad ending)
      24 → 25 (Good ending)
         → 30 (Bad ending)

[25]

"""
from collections import deque, defaultdict

good_endings = [10, 15, 25, 34]
bad_endings = [21, 30, 40]
choices = [[3, 16, 24], [16, 17, 21], [24, 25, 30]]

def find_good_endings_bfs(good_endings, bad_endings, choices):
    graph = defaultdict(list)

    for page, good, bad in choices:
        graph[page].append(good)
        graph[page].append(bad)

    start = 3
    queue = deque()

    queue.append(start)
    result = []
    while queue:
        current = queue.popleft()

        for endings in graph[current]:
            if endings in good_endings:
                result.append(endings)
            queue.append(endings)

    return result

print(find_good_endings_bfs(good_endings, bad_endings, choices))

def find_good_endings(good_endings, bad_endings, choices):
    graph = {}
    for page, good, bad in choices:
        graph[page] = [good, bad]

    print(graph)

    start = 3
    result = []
    visited = set()

    def dfs(page_num):
        visited.add(page_num)
        if page_num in good_endings:
            #print(f"{page_num} - good ending")
            result.append(page_num)
            return

        if page_num in bad_endings:
            #print(f"{page_num} is a bad ending")
            return

        if page_num not in graph:
            #print(f"{page_num} is not in the graph")
            return

        for node in graph.get(page_num, []):
            if node not in visited:
                dfs(node)

    dfs(start)

    return result


print(find_good_endings(good_endings, bad_endings, choices))