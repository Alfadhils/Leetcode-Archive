# 221. Maximal Square
## Intuition
The problem asks to find the size of the largest square containing only 1's in a binary matrix. One way to approach this problem is by using dynamic programming. We can create a 2D DP (dynamic programming) array where `dp[i][j]` represents the size of the largest square ending at cell `(i, j)`.

## Approach
1. If the cell at `(i, j)` in the matrix is '1', we update `dp[i][j]` as the minimum of the values in the adjacent cells (`dp[i-1][j]`, `dp[i][j-1]`, `dp[i-1][j-1]`) plus 1.
2. We also maintain a variable `max_len` to keep track of the maximum side length of the square encountered so far.
3. The answer would be the square of `max_len`.

## Complexity
- Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the matrix.
- Space complexity: O(m * n) for the DP array.

## Code
```python
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
```