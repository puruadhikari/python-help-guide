"""
Binary Tree
What is DFS in a Binary Tree?
DFS is a way to explore or traverse a binary tree. In DFS, you start from the root node and explore as
deep as possible along each branch before backtracking.

There are three common ways to perform DFS in a binary tree:

Preorder Traversal (Visit Root, Left, Right)
Inorder Traversal (Visit Left, Root, Right)
Postorder Traversal (Visit Left, Right, Root)

       1
      / \
     2   3
    / \   \
   4   5   6

"""
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs(node: TreeNode):
    if not node:
        return

    dfs(node.left)
    print(node.value, end=" ")
    dfs(node.right)


def bfs_binary_tree(root):
    if not root:
        return  # If the tree is empty, return immediately

    queue = deque([root])  # Initialize the queue with the root node

    while queue:
        current = queue.popleft()  # Dequeue the first node in the queue
        print(current.value, end=" ")  # Visit the node

        # Enqueue left and right children if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

dfs(root)
print("")
bfs_binary_tree(root)
