from typing import List

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
        