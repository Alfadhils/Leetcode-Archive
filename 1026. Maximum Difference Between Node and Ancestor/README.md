# 1026. Maximum Difference Between Node and Ancestor

## Intuition
The problem requires finding the maximum difference between any two nodes in a binary tree along the path from the root to a leaf. The difference is calculated as the absolute difference between the values of the maximum and minimum nodes encountered along the path.

## Approach
I will perform a depth-first search (DFS) traversal of the binary tree, keeping track of the minimum and maximum values encountered along the path from the root to the current node. At each node, I will calculate the absolute difference between the maximum and minimum values encountered so far. The maximum of these differences will be the answer.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once during the DFS traversal.
- Space complexity: O(h), where h is the height of the binary tree. The space complexity is determined by the recursive call stack during the DFS traversal.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findmaxmin(node, min_val, max_val):
            if not node:
                return abs(max_val - min_val)
            
            left_diff = findmaxmin(node.left, min(min_val,node.val), max(max_val,node.val))
            right_diff = findmaxmin(node.right, min(min_val,node.val), max(max_val,node.val))
            return max(left_diff, right_diff)

        return findmaxmin(root, float('inf'), float('-inf'))
