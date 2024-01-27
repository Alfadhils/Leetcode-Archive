from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        curr = [0]
        for i in range(n):
            prev = curr
            m = len(triangle[i])
            curr = [0]*m
            for j in range(m):
                if j == 0:
                    curr[j] = prev[j] + triangle[i][j]
                elif j == m-1:
                    curr[j] = prev[j-1] + triangle[i][j]
                else :
                    curr[j] = min(prev[j], prev[j-1]) + triangle[i][j]

        return min(curr)
        