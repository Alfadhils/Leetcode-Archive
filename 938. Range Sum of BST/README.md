# 938. Range Sum of BST

## Intuition
The problem involves finding the sum of all values in a binary search tree (BST) that fall within a given range [low, high].

## Approach
The approach taken here is to perform an inorder traversal of the BST. During the traversal, at each node, we check whether its value falls within the specified range [low, high]. If it does, we include the node's value in the sum. If the value is less than low, we only traverse the right subtree (as all values in the left subtree will also be less than low). If the value is greater than high, we only traverse the left subtree.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the BST. In the worst case, we may need to visit all nodes.
- Space complexity: The space complexity is determined by the maximum depth of the recursion stack. In the worst case, it is O(h), where h is the height of the BST. In the average case, for a balanced BST, the height is O(log n), making the space complexity O(log n).

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.inorder(root, low, high)

    def inorder(self, node, low, high):
        if not node:
            return 0

        sum_left = self.inorder(node.left, low, high)
        sum_right = self.inorder(node.right, low, high)

        if low <= node.val <= high:
            return sum_left + sum_right + node.val
        elif node.val < low:
            return sum_right
        else:
            return sum_left
