# 42. Trapping Rain Water

## Intuition

The problem involves trapping rainwater between bars. The intuition behind the solution is to use two pointers, one starting from the left and the other from the right. Move the pointers towards each other, keeping track of the maximum height encountered on each side. The amount of water that can be trapped at a particular position is determined by the minimum of the maximum heights on both sides minus the current height at that position.

## Approach

1. Initialize two pointers, `left` at the beginning of the array and `right` at the end.
2. Initialize variables `left_max` and `right_max` to track the maximum height encountered from the left and right, respectively.
3. Iterate while `left` is less than `right`.
   - If `height[left]` is less than `height[right]`, update `left_max` and calculate the trapped water at `left` position.
   - Otherwise, update `right_max` and calculate the trapped water at `right` position.
4. Move the pointers towards each other.
5. Continue the process until the pointers meet.

## Complexity

- Time complexity: O(n) - The solution iterates through the array once.
- Space complexity: O(1) - Constant space is used.

## Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                total += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                total += right_max - height[right]
                right -= 1

        return total
```
