# 463. Island Perimeter 
## Intuition
One possible intuition could be that the perimeter of an island can be calculated by counting the number of sides of each land cell that are exposed to water.

## Approach
The approach here is to iterate through each cell of the grid, and for each land cell encountered, add 4 to the perimeter count. Then, check if the cell has a neighboring land cell to its left or above. If it does, subtract 2 from the perimeter count, as those sides would not contribute to the total perimeter. Finally, return the total perimeter count.

## Complexity
- Time complexity:
The time complexity of this solution is O(rows * cols), where rows and cols are the number of rows and columns in the grid, respectively. This is because we iterate through each cell of the grid once.

- Space complexity:
The space complexity of this solution is O(1) because we are using a constant amount of extra space for storing the perimeter count and a few variables.

## Code
```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perim = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perim += 4
                    if j > 0 and grid[i][j-1] == 1:
                        perim -= 2
                    if i > 0 and grid[i-1][j] == 1:
                        perim -= 2

        return perim
```
