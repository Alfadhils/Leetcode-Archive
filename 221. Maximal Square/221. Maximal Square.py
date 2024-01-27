from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        len_x, len_y = len(matrix[0]), len(matrix)
        dp = [[0] * len_x for _ in range(len_y)]
        max_len = 0

        for i in range(len_x):
            for j in range(len_y):
                if matrix[j][i] == '1':
                    if i == 0 or j == 0:
                        dp[j][i] = 1
                    else:
                        dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
                    max_len = max(max_len, dp[j][i])

        return max_len**2