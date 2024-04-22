# 1992. Find All Groups of Farmland

## Intuition
The problem requires identifying contiguous groups of farmland in a grid. The task involves traversing the grid, identifying the starting points of each group, and extending the group boundaries until reaching non-farmland or the grid's edge.

## Approach
1. Initialize an empty result list to store the coordinates of farmland groups.
2. Traverse the grid:
   - For each cell containing farmland not visited yet:
     - Start a depth-first search (DFS) to identify the boundaries of the farmland group.
     - Extend the boundaries horizontally and vertically until reaching the edge of the farmland or encountering non-farmland.
     - Record the coordinates of the farmland group and mark all visited cells.
3. Return the list of farmland group coordinates.

## Complexity
- Time complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid. This is because we traverse each cell of the grid once.
- Space complexity: O(m * n) for the seen set to store visited cells.

## Code
``` python
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(land), len(land[0])
        seen = set()
        
        def findFarmlandCoordinates(row, col):
            coordinates = [row, col]
            r, c = row, col
            
            while r < m and land[r][col] == 1:
                r += 1
            while c < n and land[row][c] == 1:
                c += 1
            
            coordinates.extend([r - 1, c - 1])
            
            for i in range(row, r):
                for j in range(col, c):
                    seen.add((i,j))
            
            return coordinates
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i,j) not in seen:
                    result.append(findFarmlandCoordinates(i, j))
        
        return result
```