from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height_and_diameter(node):
            if not node:
                return 0

            left_height = height_and_diameter(node.left)
            right_height = height_and_diameter(node.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height_and_diameter(root)
        return self.diameter