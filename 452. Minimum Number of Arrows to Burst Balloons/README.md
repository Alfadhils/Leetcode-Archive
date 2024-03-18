# 452. Minimum Number of Arrows to Burst Balloons

## Intuition
The problem can be solved by sorting the balloons based on their end positions and then traversing through them to find the minimum number of arrows required to burst all balloons.

## Approach
1. Sort the balloons based on their end positions.
2. Initialize a variable `count` to keep track of the number of arrows required.
3. Iterate through the sorted list of balloons.
4. For each balloon, check if its start position is less than or equal to the current end position.
    - If true, update the current end position to be the minimum of the current end position and the end position of the current balloon.
    - If false, update the current end position to be the end position of the current balloon and increment the `count` variable.
5. Finally, return the `count` variable which represents the minimum number of arrows required to burst all balloons.

## Complexity
- Time complexity:
    - Sorting the balloons takes O(n log n) time.
    - Traversing through the sorted list takes O(n) time.
    - Overall time complexity: O(n log n).
- Space complexity:
    - Sorting the balloons in-place, thus no additional space is used apart from the input.
    - Space complexity: O(1).

## Code
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        curr = points[0][1]
        for start, end in points[1:]:
            if start <= curr:
                curr = min(curr, end)
            else:
                curr = end
                count += 1

        return count
```
