"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a binary tree node.

        :param val: Integer value of the node.
        :param left: Left child node.
        :param right: Right child node.
        """
        self.val = val
        self.left = left
        self.right = right


# Construct the binary tree from Example 1:
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
#      / \
#     7   4
node7 = TreeNode(7)
node4 = TreeNode(4)
node2 = TreeNode(2, node7, node4)
node6 = TreeNode(6)
node0 = TreeNode(0)
node8 = TreeNode(8)
node5 = TreeNode(5, node6, node2)
node1 = TreeNode(1, node0, node8)
root = TreeNode(3, node5, node1)

p = node5  # Node with value 5
q = node1  # Node with value 1


def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if p == root or q == root:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if p and q:
        return root

    return left if left else right


lca = lowest_common_ancestor(root, p, q)
print(lca.val)