
# 64. Minimum Path Sum

## Intuition

The problem involves finding the minimum path sum from the top-left corner to the bottom-right corner of a given grid. The idea is to use dynamic programming to efficiently calculate the minimum sum.

## Approach

The approach is based on dynamic programming, where the minimum path sum is calculated recursively, and memoization is used to store the results of subproblems to avoid redundant calculations.

1. Create a memoization table to store intermediate results.
2. Define a recursive function `dp(x, y)` to calculate the minimum path sum starting from position `(x, y)` to the bottom-right corner.
3. Check if the result for the current position is already memoized. If yes, return the memoized value.
4. If the current position is at the bottom-right corner, set the memoized value to the value in the grid at that position.
5. If the current position is on the last column, set the memoized value to the sum of the current grid value and the result of moving downward.
6. If the current position is on the last row, set the memoized value to the sum of the current grid value and the result of moving rightward.
7. Otherwise, set the memoized value to the sum of the current grid value and the minimum of moving downward or rightward.
8. Return the memoized value.

## Complexity

- Time complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid. Each cell in the grid is visited exactly once.
- Space complexity: O(m * n) for the memoization table.

## Code

```python
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
```
