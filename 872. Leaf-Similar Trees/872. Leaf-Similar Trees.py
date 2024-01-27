from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findseq(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            left_sequence = findseq(node.left)
            right_sequence = findseq(node.right)

            return left_sequence + right_sequence   

        return findseq(root1) == findseq(root2)
