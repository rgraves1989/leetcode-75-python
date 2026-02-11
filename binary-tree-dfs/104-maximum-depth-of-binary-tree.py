"""

104. Maximum Depth of Binary Tree

	Given the root of a binary tree, return its maximum depth.

	A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

	Input: root = [3,9,20,null,null,15,7]
	Output: 3

Example 2:

	Input: root = [1,null,2]
	Output: 2

Constraints:

	- The number of nodes in the tree is in the range [0, 10^4].
	- -100 <= Node.val <= 100

"""


# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def dfs(self, root: Optional[TreeNode], current_depth: int):
        current_depth += 1

        # End of the line
        if not root:
            return 0

        # DFS incrementing current_depth
        if not root.left and not root.right:
            return current_depth - 1
        elif root.left and not root.right:
            return self.dfs(root.left, current_depth)
        elif not root.left and root.right:
            return self.dfs(root.right, current_depth)
        else:
            return max(
                self.dfs(root.left, current_depth), self.dfs(root.right, current_depth)
            )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        return self.dfs(root, depth)
