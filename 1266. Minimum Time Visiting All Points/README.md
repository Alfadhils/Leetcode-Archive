# 1266. Minimum Time Visiting All Points

## Intuition
The problem requires finding the minimum time to visit all points in a 2D plane. The time taken to move from one point to another is the maximum of the absolute differences in their x and y coordinates. Intuitively, this means we want to move diagonally whenever possible to minimize the time.

## Approach
The given solution iterates through the list of points, calculates the time to move from the current point to the next one, and accumulates the total time. The time to move from one point to another is the maximum of the absolute differences in their x and y coordinates.

## Complexity
- Time complexity: O(n)
- Space complexity: O(1)

The time complexity is O(n) because we iterate through the list of points once, and for each pair of consecutive points, we perform constant-time operations.

The space complexity is O(1) because the solution uses a constant amount of extra space, regardless of the input size.

## Code
```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        prev = points[0]  
        total = 0 
        
        for point in points[1:]:
            time = max(abs(point[0] - prev[0]), abs(point[1] - prev[1]))
            total += time  
            prev = point  
        
        return total 