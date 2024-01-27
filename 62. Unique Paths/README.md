# Intuition

The problem involves finding the number of unique paths from the top-left corner to the bottom-right corner in a grid. Since you can only move down or right, this problem exhibits optimal substructure, making it suitable for a dynamic programming solution.

# Approach

The approach here is to use dynamic programming with memoization. The idea is to define a recursive function `dp(x, y, memo)` that represents the number of unique paths from the top-left corner to the cell `(x, y)`. The base cases are when `x` or `y` is 1, in which case there is only one path (either moving right or down). Otherwise, the recursive formula is used: `dp(x, y) = dp(x - 1, y) + dp(x, y - 1)`. The memo dictionary is used to store previously computed values to avoid redundant calculations.

# Complexity

- Time complexity: O(m * n) - Each cell in the m x n grid is calculated once, and the results are memoized for future use.
- Space complexity: O(m * n) - The memo dictionary stores the results for each cell in the grid.

# Code

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(x, y, memo):
            key = tuple(sorted((x, y)))

            if key in memo:
                return memo[key]

            if x == 1 or y == 1:
                return 1

            memo[key] = dp(x - 1, y, memo) + dp(x, y - 1, memo)
            return memo[key]

        return dp(m, n, {})
```
