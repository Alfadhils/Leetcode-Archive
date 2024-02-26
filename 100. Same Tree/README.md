# 100. Same Tree

## Intuition
The problem asks whether two binary trees are structurally identical and have the same node values at corresponding positions. We note that a tree is identical if its branch is also identical.

## Approach
The approach is to traverse both trees simultaneously and compare their nodes at each step. If the current nodes being compared are both None, return True as it indicates the end of both trees. If one of the nodes is None while the other is not, return False, as it indicates a mismatch in the structure. If the values of the current nodes are not equal, return False. Otherwise, recursively compare the left subtrees and right subtrees of both trees.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the tree. We need to visit each node once.
- Space complexity: O(h), where h is the height of the tree. The space complexity is determined by the recursive call stack. In the worst case, the height of the tree could be equal to the number of nodes in the tree, resulting in O(n) space complexity.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
