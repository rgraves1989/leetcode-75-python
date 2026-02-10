"""

1448. Count Good Noes in Binary Tree

"""


# Time complexity: O()
# Space complexity: O()
class Solution:
    def traverseWithMax(self, node: TreeNode, maxSoFar: int) -> int:
        # End of the line
        if not node:
            return 0

        # Leaf
        if not node.left and not node.right:
            return 1 if maxSoFar <= node.val else 0

        # Not a leaf, keep traversing...
        is_current_good = 1 if maxSoFar <= node.val else 0
        return (
            is_current_good
            + self.traverseWithMax(node.left, max(maxSoFar, node.val))
            + self.traverseWithMax(node.right, max(maxSoFar, node.val))
        )

    def goodNodes(self, root: TreeNode) -> int:
        return self.traverseWithMax(root, root.val)
