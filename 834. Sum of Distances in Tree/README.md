# 834. Sum of Distances in Tree

## Intuition
The problem involves finding the sum of distances between all pairs of nodes in a tree. One intuitive approach is to perform two depth-first searches (DFS) to compute the required distances efficiently.

## Approach
1. Build an adjacency list representation of the tree.
2. Perform a DFS to compute two arrays:
   - `count`: the number of nodes in the subtree rooted at each node.
   - `res`: the sum of distances from the current node to all other nodes in the subtree rooted at it.
3. Perform a second DFS to update the `res` array:
   - For each node, update the sum of distances based on its parent node's sum and the number of nodes in its subtree.
4. Return the `res` array.

## Complexity
- Time complexity: Both DFS traversals take O(N) time, where N is the number of nodes in the tree.
- Space complexity: The space complexity is O(N) to store the adjacency list and additional arrays `count` and `res`.
  
## Code
```python
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = [0] * N
        res = [0] * N
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs1(cur: int, parent: int) -> None:
            count[cur] = 1
            for child in graph[cur]:
                if child != parent:
                    dfs1(child, cur)
                    count[cur] += count[child]
                    res[cur] += res[child] + count[child]
        
        def dfs2(cur: int, parent: int) -> None:
            for child in graph[cur]:
                if child != parent:
                    res[child] = res[cur] + N - 2 * count[child]
                    dfs2(child, cur)
        
        dfs1(0, -1)
        dfs2(0, -1)
        
        return res
```