from typing import List

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