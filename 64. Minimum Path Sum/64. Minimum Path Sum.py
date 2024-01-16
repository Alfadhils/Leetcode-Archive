from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_x, len_y = len(grid[0]), len(grid)
        memo = [[-1] * len_x for _ in range(len_y)]

        def dp(x, y):
            if memo[y][x] != -1:
                return memo[y][x]

            if x == len_x - 1 and y == len_y - 1:
                memo[y][x] = grid[y][x]
            elif x == len_x - 1:
                memo[y][x] = grid[y][x] + dp(x, y + 1)
            elif y == len_y - 1:
                memo[y][x] = grid[y][x] + dp(x + 1, y)
            else:
                memo[y][x] = grid[y][x] + min(dp(x + 1, y), dp(x, y + 1))

            return memo[y][x]

        return dp(0, 0)
        