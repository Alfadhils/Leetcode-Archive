# 872. Leaf-Similar Trees

## Intuition
The problem asks to determine whether the leaf sequence of two binary trees is the same. The leaf sequence of a binary tree is the sequence of leaf nodes from left to right. We need to check if the leaf sequences of two given binary trees, `root1` and `root2`, are identical.

## Approach
To solve this problem, we can perform a depth-first search (DFS) on both trees to extract their leaf sequences. We can define a recursive function `findseq` that takes a node as an input and returns the leaf sequence of that subtree.

The base case of the recursion is when the node is `None`, in which case an empty list is returned. If the node is a leaf (i.e., it has no left or right children), we return a list containing the value of that leaf node.

For non-leaf nodes, we recursively call `findseq` on the left and right children and concatenate their leaf sequences.

Finally, we compare the leaf sequences of the two trees obtained using the `findseq` function. If the sequences are equal, the function returns `True`; otherwise, it returns `False`.

## Complexity
- Time complexity: The `findseq` function visits each node once, so the time complexity is O(n), where n is the total number of nodes in both trees.
- Space complexity: The space complexity is also O(n), as we use recursion to traverse the tree, and the maximum depth of the recursion is the height of the tree.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findseq(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            left_sequence = findseq(node.left)
            right_sequence = findseq(node.right)

            return left_sequence + right_sequence   

        return findseq(root1) == findseq(root2)
