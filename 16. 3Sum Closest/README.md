# 16. 3Sum Closest

## Intuition

The problem requires finding the closest sum of three integers to the target value in an array. To solve this, we can use a two-pointer approach along with sorting the array.

## Approach

1. Sort the input array.
2. Iterate through the array.
3. Use two pointers approach for the remaining elements (start and end) after the current element in the iteration.
4. Calculate the sum of three elements and update the result if the current sum is closer to the target than the previous closest sum.
5. Adjust the pointers based on the comparison of the current sum with the target.

## Complexity

- Time complexity: O(n^2) - The sorting takes O(n log n) time, and the two-pointer traversal takes O(n) time.
- Space complexity: O(1) - Constant space is used.

## Code

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        diff = float('inf')
        nums.sort()
        val = 0

        for i in range(0, n):
            start, end = i + 1, n - 1

            while start < end:
                threeSum = nums[i] + nums[start] + nums[end]
                res = abs(threeSum - target)

                if res == 0:
                    return threeSum

                if res < diff:
                    diff = res
                    val = threeSum

                if threeSum < target:
                    start += 1
                else:
                    end -= 1

        return val
```
