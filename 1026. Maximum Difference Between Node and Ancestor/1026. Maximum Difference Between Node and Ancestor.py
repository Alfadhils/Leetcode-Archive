from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findmaxmin(node, min_val, max_val):
            if not node:
                return abs(max_val - min_val)
            
            left_diff = findmaxmin(node.left, min(min_val,node.val), max(max_val,node.val))
            right_diff = findmaxmin(node.right, min(min_val,node.val), max(max_val,node.val))
            return max(left_diff, right_diff)

        return findmaxmin(root, float('inf'), float('-inf'))
        