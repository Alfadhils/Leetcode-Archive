# Intuition

The problem can be approached using dynamic programming to find the number of unique paths in a grid with obstacles.

# Approach

The approach involves creating a recursive function (`dp`) that calculates the number of unique paths for a given position (`x, y`) on the grid. The function uses memoization to store already computed results and avoid redundant calculations.

# Complexity

- Time complexity: O(m * n), where m is the number of columns and n is the number of rows in the obstacleGrid.
- Space complexity: O(m * n), as the memo dictionary can have at most m * n entries.


# Code

```python
classSolution:
    defuniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        len_x, len_y = len(obstacleGrid[0]), len(obstacleGrid)
    
        defdp(x, y, memo):
            key = (x, y)

            if obstacleGrid[y - 1][x - 1]:
                memo[key] = 0
            elif key in memo:
                return memo[key]
            elif x == 1and y == 1:
                memo[key] = 1
            elif x == 1:
                memo[key] = dp(x, y - 1, memo)
            elif y == 1:
                memo[key] = dp(x - 1, y, memo)
            else:
                memo[key] = dp(x - 1, y, memo) + dp(x, y - 1, memo)

            return memo[key]

        return dp(len_x, len_y, {})
```
