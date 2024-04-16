# 404. Sum of Left Leaves

## Intuition
My initial thought is to perform a depth-first traversal of the binary tree while keeping track of whether each node is a left child or not. If a node is a leaf node and a left child, we add its value to the sum.

## Approach
I'll define a recursive function `traverseLeft` that takes a node and a boolean flag indicating whether the node is a left child. Inside this function, I'll check if the current node is a leaf node and a left child. If it is, I'll add its value to the sum. Then, I'll recursively call `traverseLeft` on the left and right children, updating the flag accordingly.

## Complexity
- Time complexity:
  - The time complexity of this approach is O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
  
- Space complexity:
  - The space complexity is also O(n) in the worst case, where n is the number of nodes in the binary tree. This space is used for the recursive call stack.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverseLeft(root, isLeft):
            if not root: 
                return 0

            if not root.left and not root.right and isLeft: 
                return root.val

            return traverseLeft(root.left, True) + traverseLeft(root.right, False)
        
        return traverseLeft(root, False)
```