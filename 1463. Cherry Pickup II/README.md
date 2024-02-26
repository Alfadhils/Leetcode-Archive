# 1463. Cherry Pickup II

## Intuition
This problem seems to be a dynamic programming problem where we need to maximize the number of cherries picked by two people moving through the grid. We can approach this by breaking down the problem into smaller subproblems and using memoization to avoid redundant calculations.

## Approach
1. Initialize the necessary variables including the grid dimensions and a memoization dictionary.
2. Define a recursive function `dp` that takes the current row and the positions of both people (`i` and `j`) as arguments.
3. Within the `dp` function, handle the base case where we've reached the last row, in which case we return 0 as there are no more cherries to pick.
4. Check if we've already computed the maximum value for the current state `(row, i, j)` using memoization. If so, return the memoized value.
5. Calculate the value of cherries picked by both people at their current positions.
6. Initialize a variable `max_val` to store the maximum value of cherries picked.
7. Iterate through all possible moves for both people within the grid and recursively calculate the maximum value of cherries picked by considering all possible paths.
8. Update the `max_val` with the maximum value obtained from all possible moves.
9. Memoize the calculated maximum value for the current state `(row, i, j)` and return it.
10. Return the result of the `dp` function called with initial parameters `(0, 0, cols - 1)` which represent starting positions for both people at the first row.

## Complexity
- Time complexity:
  - The time complexity of this approach is O(n^3), where n is the number of columns in the grid. This is because for each cell in the grid, we explore all possible movements of both people in the next row, resulting in a total of O(n^3) operations.
- Space complexity:
  - The space complexity is also O(n^3) due to the memoization dictionary storing results for each unique state `(row, i, j)`.

## Code
``` python
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
```