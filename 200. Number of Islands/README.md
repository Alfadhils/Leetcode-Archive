# 200. Number of Islands

## Intuition
The problem can be approached using a depth-first search (DFS) technique to traverse the grid and identify connected components or islands.

## Approach
1. Define a helper function `expand(i, j)` that performs a DFS traversal to expand from the current cell `(i, j)` to neighboring cells with the value '1'.
2. Iterate through each cell in the grid.
3. If the cell contains '1' and has not been visited before, increment the count of islands and call the `expand` function to explore the connected component.
4. Within the `expand` function, mark visited cells and recursively explore neighboring cells.

## Complexity
- Time complexity: 
  - The function `expand` has a time complexity of O(rows * cols) in the worst case, where rows and cols are the dimensions of the grid.
  - Overall, the time complexity of the algorithm is O(rows * cols) as each cell is visited once.
- Space complexity:
  - The space complexity is O(rows * cols) due to the recursion stack and the set `seen` used to track visited cells.

## Code
``` python
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
```