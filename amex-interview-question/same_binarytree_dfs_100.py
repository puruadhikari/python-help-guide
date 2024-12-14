# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node, node_list):
            if not node:
                return

            dfs(node.left, node_list)
            node_list.append(node.val)
            dfs(node.right, node_list)

            return node_list

        p_list = []
        q_list = []
        p_list = dfs(p, p_list)
        q_list = dfs(q, q_list)

        return p_list == q_list


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

sol = Solution()

print(sol.isSameTree(root1, root2))

