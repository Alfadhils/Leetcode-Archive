from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def expand(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or (i, j) in seen:
                return
            seen.add((i, j))
            expand(i + 1, j)
            expand(i - 1, j)
            expand(i, j + 1)
            expand(i, j - 1)
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        seen = set()
        num_islands = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in seen:
                    num_islands += 1
                    expand(i, j)
                    
        return num_islands