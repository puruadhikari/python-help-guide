class Node:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None


def get_depth(root_node: Node):
    if not root_node:
        return 0
    left_depth = get_depth(root_node.left)
    right_depth = get_depth(root_node.right)

    return max(left_depth, right_depth) + 1

from collections import deque

def get_depth_bfs(node):
    if not node:
        return 0
    queue = deque()
    queue.append((node,1))
    max_level = 1
    level = 0

    while queue:
        current, level = queue.popleft()
        max_level = max(level,max_level)
        if current.left:
            queue.append((current.left,max_level+1))
        if current.right:
            queue.append((current.right,max_level+1))

    return max_level


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.left.right = Node(7)

print(get_depth(root))
print(get_depth_bfs(root))