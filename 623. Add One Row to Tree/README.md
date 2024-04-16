# 623. Add One Row to Tree
## Intuition
The problem requires adding a row of nodes with a given value at a specified depth in a binary tree. To accomplish this, we can traverse the tree using breadth-first search (BFS), maintaining the depth of each node. When we reach the desired depth, we insert new nodes with the given value as the new row.

## Approach
1. If the tree is empty, return a new node with the given value if the depth is 1, otherwise return None.
2. If the depth is 1, create a new node with the given value and set the current root as its left child. Return the new root.
3. Initialize a queue with tuples containing nodes and their respective depths.
4. Traverse the tree using BFS:
   - If the current depth is one less than the desired depth, insert new nodes with the given value as the new row.
   - Continue BFS until reaching the desired depth.
5. Return the modified root.

## Complexity
- Time complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once.
- Space complexity: O(n), where n is the maximum number of nodes at any level in the binary tree. This is the space required for the queue during BFS traversal.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```
