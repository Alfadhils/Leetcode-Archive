from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        len_x, len_y = len(matrix[0]), len(matrix)

        dp = [[0] * len_x for _ in range(len_y)]

        for y in range(len_y):
            for x in range(len_x):
                if y == 0:
                    dp[y][x] = matrix[y][x]
                elif x == 0:
                    dp[y][x] = min(dp[y-1][x], dp[y-1][x+1]) + matrix[y][x]
                elif x == len_x-1:
                    dp[y][x] = min(dp[y-1][x], dp[y-1][x-1]) + matrix[y][x]
                else :
                    dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y-1][x+1]) + matrix[y][x]

        return min(dp[-1])
        