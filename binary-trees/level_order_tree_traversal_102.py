"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def level_order_tree_traversal(root):
    if not root:
        return []
    queue = deque()
    queue.append(root)
    result = []

    while queue:
        inner_result = []
        for _ in range(len(queue)):
            current = queue.popleft()
            inner_result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(inner_result)

    return result

print(level_order_tree_traversal(root))