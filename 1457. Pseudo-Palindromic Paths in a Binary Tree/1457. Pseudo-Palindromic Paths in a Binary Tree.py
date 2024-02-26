from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dp(node, pairs):
            if not node:
                return

            if node.val in pairs:
                pairs.remove(node.val)
            else :
                pairs.add(node.val)

            if not node.left and not node.right:
                if len(pairs)<2:
                    self.count += 1

            dp(node.left, pairs.copy())
            dp(node.right, pairs.copy())

        dp(root, set())
        return self.count