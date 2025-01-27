"""
You work in an automated robot factory. Once robots are assembled, they are sent to the shipping center
via a series of autonomous delivery carts, each of which moves packages on a one-way route.
Given input that provides the (directed) steps that each cart takes as pairs, write a function that
identifies all the start locations, and a collection of all the possible ending locations for each start.
Your goal is to identify all starting locations (nodes with no incoming paths) and, for each starting location,
determine all possible unique ending locations (nodes with no outgoing paths) reachable from that starting location.
Input:
A list of pairs paths, where each pair [start, end] represents a one-way route from start to end.

Output:
A dictionary where:
Keys are starting locations (nodes with no incoming edges).
Values are lists of all unique ending locations (nodes with no outgoing edges) reachable from the corresponding start.

Input is path1 shown below
Output is :
{
'A': ['K'],
'E': ['H', 'I', 'L'],
'J': ['M']
}
"""

from collections import defaultdict

paths1 = [
    ["A", "B"], ["A", "C"],
    ["B", "K"],
    ["C", "K"],
    ["E", "L"],
    ["E", "F"], ["F", "G"],
    ["G", "H"], ["G", "I"],
    ["J", "M"]
]

def find_paths(paths):
    graph = defaultdict(list)

    for origin, destination in paths:
        graph[origin].append(destination)

    a_set = set()
    start_set = set()

    for items in graph.values():
        for item in items:
            a_set.add(item)

    for key, values in graph.items():
        if key not in a_set:
            start_set.add(key)

    def dfs(start, graph, visited):
        if start in visited:
            return
        if start not in graph:
            temp_result.append(start)
            return temp_result
        visited.add(start)
        for item in graph[start]:
            dfs(item, graph, visited)
        return set(temp_result)

    result = {}
    for items in start_set:
        visited = set()
        temp_result = []
        val = dfs(items, graph, visited)
        result[items] = list(val)
    return result


print(find_paths(paths1))
