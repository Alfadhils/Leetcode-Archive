# 988. Smallest String Starting From Leaf

## Intuition
The problem requires finding the lexicographically smallest string that starts from a leaf in a binary tree.

## Approach
We can perform a depth-first search (DFS) traversal of the binary tree, keeping track of the path from the root to the current node. While traversing, we construct the string representing the path by appending characters corresponding to the node values. When we reach a leaf node, we compare the constructed string with the current smallest string found so far and update it if necessary. Finally, we return the smallest string found.

## Complexity
- Time complexity:
  - The DFS traversal visits each node once, so the time complexity is O(n), where n is the number of nodes in the binary tree.
- Space complexity:
  - The space complexity is also O(n) due to the recursive calls on the call stack.

## Code
```python
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        def dfs(root, path=''):
            nonlocal res
            if not root:
                return
            
            path += chr(ord('a') + root.val)
            
            if not root.left and not root.right:
                if not res :
                    res = path[::-1]
                else :
                    res = min(path[::-1], res)
            
            if root.left:
                dfs(root.left, path)
            
            if root.right:
                dfs(root.right, path)
            
            path = path[:-1]
        
        dfs(root)
        return res
```