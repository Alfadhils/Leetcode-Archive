from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        curr = points[0][1]
        for start, end in points[1:]:
            if start <= curr:
                curr = min(curr, end)
            else :
                curr = end
                count += 1

        return count