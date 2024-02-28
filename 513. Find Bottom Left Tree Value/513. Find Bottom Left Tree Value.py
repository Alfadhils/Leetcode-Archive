from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            if node is None:
                return

            queue = [[node, 0]]
            maxlen = 0
            res = node.val

            while queue:
                curr, length = queue.pop(0)
                if length > maxlen:
                    maxlen = length
                    res = curr.val

                if curr.left:
                    queue.append([curr.left, length+1])
                if curr.right:
                    queue.append([curr.right, length+1])

            return res

        return bfs(root)
        