from typing import List
from collections import defaultdict, deque

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