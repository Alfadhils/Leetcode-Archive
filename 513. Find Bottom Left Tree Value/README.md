# 513. Find Bottom Left Tree Value
## Intuition
The problem asks to find the value of the leftmost node in the last row of a binary tree. To solve this problem, a straightforward approach is to perform a breadth-first search (BFS) traversal of the binary tree. By traversing the tree level by level, we can keep track of the leftmost node at each level and eventually return the value of the leftmost node in the last level encountered during the traversal.

## Approach
To implement the approach described above, we define a helper function bfs that performs a breadth-first search traversal of the binary tree. Within this function, we maintain a `queue` to store nodes along with their corresponding levels. We initialize the `maxlen` variable to keep track of the maximum level encountered so far, and the `res` variable to store the value of the leftmost node in the last row.

During the traversal, for each node popped from the `queue`, we check if its level is greater than the current `maxlen`. If so, we update `maxlen` and update `res` with the value of the current node. We then enqueue the left and right child nodes (if they exist) along with their corresponding levels incremented by 1.

Finally, we return the value stored in `res`, which represents the value of the leftmost node in the last row of the binary tree.

## Complexity
- Time complexity: 
O(n), where `n` is the number of nodes in the binary tree. This is because we visit each node once during the breadth-first search traversal.
- Space complexity: 
O(n), where `n` is the number of nodes in the binary tree. In the worst case, the queue can contain all nodes of the last level of the binary tree.

## Code
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
        
```