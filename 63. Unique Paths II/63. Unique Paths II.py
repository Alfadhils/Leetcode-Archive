from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        len_x, len_y = len(obstacleGrid[0]), len(obstacleGrid)
        
        def dp(x, y, memo):
            key = (x,y)

            if obstacleGrid[y-1][x-1]:
                memo[key] = 0
            elif key in memo:
                return memo[key]
            elif x == 1 and y == 1:
                memo[key] = 1
            elif x == 1 :
                memo[key] = dp(x,y-1,memo)
            elif y == 1 :
                memo[key] = dp(x-1,y,memo)
            else :
                memo[key] = dp(x - 1, y, memo) + dp(x, y - 1, memo)

            return memo[key]

        return dp(len_x, len_y, {})
        