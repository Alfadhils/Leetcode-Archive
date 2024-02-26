from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dp(row, i, j):
            if row == rows:
                return 0
            if (row,i,j) in memo:
                return memo[(row,i,j)]
            
            val = grid[row][i] + (grid[row][j] if i != j else 0)
            max_val = 0
            for x in [i - 1, i, i + 1]:
                for y in [j - 1, j, j + 1]:
                    if 0 <= x < cols and 0 <= y < cols:
                        max_val = max(max_val, val + dp(row + 1, x, y))
            memo[(row,i,j)] = max_val
            return max_val

        return dp(0, 0, cols - 1)