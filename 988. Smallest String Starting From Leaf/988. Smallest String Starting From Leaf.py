from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        def dfs(root, path=''):
            nonlocal res
            if not root:
                return
            
            path += chr(ord('a') + root.val)
            
            if not root.left and not root.right:
                if not res :
                    res = path[::-1]
                else :
                    res = min(path[::-1], res)
            
            if root.left:
                dfs(root.left, path)
            
            if root.right:
                dfs(root.right, path)
            
            path = path[:-1]
        
        dfs(root)
        return res

        