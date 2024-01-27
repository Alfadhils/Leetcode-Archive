from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.inorder(root, low, high)

    def inorder(self, node, low, high):
        if not node:
            return 0

        sum_left = self.inorder(node.left, low, high)
        sum_right = self.inorder(node.right, low, high)

        if low <= node.val <= high:
            return sum_left + sum_right + node.val
        elif node.val < low:
            return sum_right
        else:
            return sum_left
