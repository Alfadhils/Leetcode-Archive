from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        total = 0
        for point in points[1:]:
            time = max(abs(point[0]-prev[0]),abs(point[1]-prev[1]))
            total += time
            prev = point
        
        return total
        