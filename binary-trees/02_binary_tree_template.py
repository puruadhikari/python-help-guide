from collections import deque
"""
IMP NOTE : use this template to get levels, sum in levels etc. 
"""

class Node:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.left.right = Node(7)


def get_bfs_values(root):
    queue = deque()
    queue.append(root)
    level = []

    while queue:
        level_items = []
        for _ in range(len(queue)):
            current = queue.popleft()
            level_items.append(current.node)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        level.append(level_items)

    return level


print(get_bfs_values(root))