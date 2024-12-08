class Node:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None


def good_nodes(root_node: Node, max_val):
    if not root_node:
        return 0

    if root_node.node >= max_val:
        is_good = 1
    else:
        is_good = 0

    new_max_val = max(max_val, root_node.node)
    left_side = good_nodes(root_node.left, new_max_val)
    right_side = good_nodes(root_node.right, new_max_val)

    return left_side + is_good + right_side


root = Node(3)
root.left = Node(1)
root.right = Node(4)

root.left.left = Node(3)

root.right.left = Node(1)
root.right.left.right = Node(5)

print(good_nodes(root, float('-inf')))