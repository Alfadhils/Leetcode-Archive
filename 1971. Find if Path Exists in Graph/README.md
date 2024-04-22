# 1971. Find if Path Exists in Graph

## Intuition
The problem asks whether there exists a path between a given source and destination in a graph. To solve this, we can use depth-first search (DFS) to traverse the graph from the source node and check if we can reach the destination node.

## Approach
We'll represent the graph using an adjacency list. Then, we'll perform a DFS from the source node, marking visited nodes to avoid cycles. During the DFS traversal, if we encounter the destination node, we return True, indicating that a path exists between the source and destination nodes. Otherwise, we return False if no such path is found.

## Complexity
- Time complexity:
    - Building the adjacency list: O(E) where E is the number of edges.
    - DFS traversal: O(V + E) where V is the number of vertices and E is the number of edges.
    - Total time complexity: O(V + E)
- Space complexity:
    - Adjacency list: O(V + E)
    - Set for visited nodes: O(V)
    - Total space complexity: O(V + E)

## Code
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {}
        visit = set()
        for left,right in edges:
            adj.setdefault(left, []).append(right)
            adj.setdefault(right, []).append(left)

        def dfs(a,b) :
            if a == b :
                return True
            
            visit.add(a)
            for neighbor in adj.get(a, []):
                if neighbor not in visit:
                    if dfs(neighbor,b):
                        return True

            return False

        return dfs(source,destination)
