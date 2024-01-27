# Intuition
The problem involves finding the minimum path sum from the top to the bottom of a triangle. Each step, you can move to an adjacent number in the row below. The intuition is to use dynamic programming to efficiently compute the minimum path sum.

# Approach
The approach involves using dynamic programming to build up the minimum path sum from the bottom to the top of the triangle. We maintain an array `curr` to represent the minimum path sum for each element in the current row. For each row, we update `curr` based on the minimum path sum from the previous row. We iterate through each element in the row, calculating the minimum path sum by considering the adjacent elements in the row above.

# Complexity
- Time complexity: O(n^2), where n is the number of rows in the triangle. This is because we iterate through each element in the triangle, and for each element, we perform constant time operations.
- Space complexity: O(n), where n is the number of rows in the triangle. We use a 1D array `curr` to store the minimum path sum for each element in the current row.

# Code
```python
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
                else:
                    curr[j] = min(prev[j], prev[j-1]) + triangle[i][j]

        return min(curr)
