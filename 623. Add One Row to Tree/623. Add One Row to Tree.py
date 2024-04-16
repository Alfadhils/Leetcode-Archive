from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val) if depth == 1 else None

        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node

        queue = [(root, 1)]

        while queue:
            node, current_depth = queue.pop(0)

            if current_depth == depth - 1:
                while True :
                    new_node = TreeNode(val)
                    new_node.left = node.left
                    node.left = new_node
                    
                    new_node = TreeNode(val)
                    new_node.right = node.right
                    node.right = new_node
                    
                    if not queue:
                        break
                    else :
                        node, current_depth = queue.pop(0)
                
                return root

            if node.left:
                queue.append((node.left, current_depth + 1))
            if node.right:
                queue.append((node.right, current_depth + 1))

        return root
        