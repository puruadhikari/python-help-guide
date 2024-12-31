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


def level_order_tree_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []

