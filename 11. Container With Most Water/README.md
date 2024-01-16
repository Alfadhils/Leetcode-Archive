# 11. Container With Most Water

## Intuition

The problem asks to find the maximum area that can be formed by choosing two lines from an array of heights. The area is determined by the minimum height of the two lines and the distance between them.

## Approach

We can use a two-pointer approach to solve this problem efficiently. Initialize two pointers, `left` at the beginning of the array and `right` at the end. Calculate the area formed by the lines at these positions, and then move the pointers towards each other. At each step, update the maximum area based on the minimum height between the lines and the reduced width. Continue this process until the pointers meet.

## Complexity

- Time complexity: O(n) - The two pointers move towards each other at most n steps, where n is the number of elements in the array.
- Space complexity: O(1) - We are using constant space to store variables.

## Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```
