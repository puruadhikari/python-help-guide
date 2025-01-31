class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        first, last = None, None

        def in_order_traversal(node):
            nonlocal first, last
            if not node:
                return

            # Left (in-order traversal)
            in_order_traversal(node.left)

            # Process node
            if last:
                last.right = node  # Link last node to current node
                node.left = last
            else:
                first = node  # First node in DLL

            last = node  # Update last to current node

            # Right (in-order traversal)
            in_order_traversal(node.right)

        in_order_traversal(root)

        # Connect first and last to make it circular
        first.left = last
        last.right = first

        return first
