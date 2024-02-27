# 543. Diameter of Binary Tree

## Intuition
The diameter of a binary tree is defined as the number of nodes on the longest path between any two nodes in the tree. One way to find the diameter is to consider each node as a potential root of the subtree and calculate the maximum diameter among all subtrees. 

## Approach
We can use a recursive approach to calculate both the height and diameter of each subtree in a single pass. By recursively computing the height of left and right subtrees, we can then calculate the diameter of the subtree rooted at each node by adding their heights. We update the diameter if the sum of the heights is greater than the current diameter.

## Complexity
- Time complexity: O(n) where n is the number of nodes in the binary tree. This is because we visit each node once.
- Space complexity: O(h) where h is the height of the binary tree. This is due to the recursive calls on the stack, which can go as deep as the height of the tree.

## Code
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height_and_diameter(node):
            if not node:
                return 0

            left_height = height_and_diameter(node.left)
            right_height = height_and_diameter(node.right)

            # Update the diameter if the sum of left height and right height is greater
            self.diameter = max(self.diameter, left_height + right_height)

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        height_and_diameter(root)
        return self.diameter
```