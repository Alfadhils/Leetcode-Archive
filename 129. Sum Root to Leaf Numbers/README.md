# 129. Sum Root to Leaf Numbers
## Intuition
The problem requires calculating the sum of all root-to-leaf numbers represented by a binary tree. The intuition is to traverse the tree using depth-first search (DFS) and maintain a current sum along the path. When reaching a leaf node, add the current sum to the total sum.

## Approach
We start with a total sum initialized to 0. Then, we perform a DFS traversal of the tree, maintaining the current sum. At each node, we update the current sum by appending the node's value and continue traversing left and right. When we reach a leaf node, we add the current sum to the total sum. Finally, we return the total sum.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node exactly once.
- Space complexity: O(h), where h is the height of the binary tree. In the worst case, the space complexity is O(n) for a skewed tree.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```