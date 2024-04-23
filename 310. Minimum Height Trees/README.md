# 310. Minimum Height Trees

## Intuition
The problem asks to find the minimum height trees in a graph given its edges. One way to approach this problem is by iteratively removing leaves (nodes with only one neighbor) until there are only 1 or 2 nodes left. The remaining nodes would form the minimum height trees.

## Approach
- First, handle the special case when there's only one node in the graph.
- Then, construct the graph using a defaultdict of sets to store the neighbors of each node.
- Identify the leaves (nodes with only one neighbor) and store them in a deque.
- Iterate while there are more than 2 nodes:
  - Remove the current leaves from the graph and update the neighboring nodes.
  - Add the new leaves (nodes with only one neighbor) to the deque.
- Return the remaining nodes, which are the roots of the minimum height trees.

## Complexity
- Time complexity: O(n), where n is the number of nodes. Constructing the graph takes O(n), and each iteration of removing leaves takes O(n).
- Space complexity: O(n), where n is the number of nodes. The space is mainly used for storing the graph, leaves, and new leaves.

## Code
``` python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque([node for node, neighbors in graph.items() if len(neighbors) == 1])

        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            while leaves:
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop() 
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)
```