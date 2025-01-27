"""
You are given input data that represents a graph of relationships between parents and children over multiple generations.
The data is structured as a list of (parent, child) pairs, where each individual is identified by a unique positive integer.

For a given individual, write a function findEarliestAncestor(parentChildPairs, individual) that returns their
earliest known ancestor, defined as the ancestor farthest away from the individual in terms of generations.

Rules:
If there is more than one ancestor tied for "earliest," return any one of them.
If the input individual has no parents, return null or -1.
"""
parentChildPairs1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4)
]

# findEarliestAncestor(parentChildPairs1, 8)
def find_earliest_ancestor(parent_child_paris,target):
    graph = {}

    for parent, child in parent_child_paris:
        if child not in graph:
            graph[child] = [parent]
        else:
            graph[child].append(parent)
    result = dfs(graph,target)
    if result == target:
        return -1

    return result

def dfs(graph1, number):
    if number not in graph1:
        return number

    # earliest_ancestor = None
    for items in graph1[number]:
        ancestor = dfs(graph1, items)

    # # edge case when two items are found but not sure.
    # if earliest_ancestor is None or ancestor < earliest_ancestor:
    #     earliest_ancestor = ancestor

    return ancestor


print(find_earliest_ancestor(parentChildPairs1, 8))