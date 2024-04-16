from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        
        def dfs(node, current_sum=0):
            nonlocal total_sum
            if node is None:
                return
        
            current_sum = current_sum * 10 + node.val
            
            if node.left is None and node.right is None:
                total_sum += current_sum
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        dfs(root)

        return total_sum